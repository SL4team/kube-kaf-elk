import json

inout_f = open("C:/Users/slinfo/Desktop/seoul_school.csv", 'r', encoding="UTF-8")
inout_lines = inout_f.readlines()

json_f = open("C:/Users/slinfo/Desktop/seoul_school1.json", 'w', encoding="UTF-8")

for i in inout_lines:
    school_name = i.split(',')[0]
    school_sort = i.split(',')[1]
    school_type = i.split(',')[3]
    addr = i.split(',')[4]
    lat = i.split(',')[5]
    lon = i.split(',')[6]
    # print(brand)
    data = {
        "school_name": school_name,
        "school_sort": school_sort,
        "school_type": school_type,
        "addr": addr,
        "school_geo": {"lat": lat, "lon": lon}
    }
    json_f.write(json.dumps(data, ensure_ascii=False) + "\n")


inout_f.close()
json_f.close()
