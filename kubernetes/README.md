# [ 쿠버네티스 환경 구성 과정 _ ubuntu18.04]

# 필수 구성요소 설치

cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

# 필요한 sysctl 파라미터를 설정하면 재부팅 후에도 유지된다.
cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

# 재부팅하지 않고 sysctl 파라미터 적용
sudo sysctl --system

# containerd(런타임) 설치 - 도커 지원 중단에 따른 방안

sudo apt-get update 

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install containerd.io

sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd

# 3. systemd croup 드라이버 사용

vi /etc/containerd/config.toml
에서 SystemdCgroup =false -> true 로 변경

 [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true

sudo systemctl restart containerd

# 4. 쿠버네티스 설치

sudo apt-get update
sudo apt-get upgrade

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl

# 5. 마스터 노드 세팅

sudo kubeadm init --pod-network-cidr=[파드의 네트워크 대역대 설정] --apiserver-advertise-address=[ 마스터노드 ip 설정 ] --cri-socket /run/containerd/containerd.sock

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config


# 5-1. 워커 노드 세팅
마스터노드에서 init 시 발행한 join 명령어 실행

kubeadm join [마스터 노드 ip] --token [ 토큰 ] \
	--discovery-token-ca-cert-hash sha256:[해쉬값] --cri-socket /run/containerd/containerd.sock

# 6. calico설치

wget https://docs.projectcalico.org/manifests/calico.yaml
sed -i -e 's?192.168.0.0/16?(클러스터 내부적으로 사용할 네트워크 대역)?g' calico.yaml
kubectl apply -f calico.yaml
