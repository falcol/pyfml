"""Viết script tìm 50 quán bia / quán nhậu / quán bar / nhà hàng
quanh toạ độ của lớp học (lên google map để lấy) với bán kính 2KM.
Ghi kết quả theo định dạng JSON vào file pymi_beer.geojson

Sử dụng Google Map API
https://developers.google.com/places/web-service/

Chú ý: phải tạo "token" để có thể truy cập API.

Chú ý: giữa mỗi trang kết quả phải đợi để lấy tiếp.

Chú ý: tránh đặt ngược lat/long
location: 21.012985,105.821839
- Kết quả trả về lưu theo format JSON, với mỗi điểm là một GeoJSON point
(https://leafletjs.com/examples/geojson/),
up file này lên GitHub để xem bản đồ kết quả.
- Xem mẫu GEOJSON https://github.com/tung491/make_boba_map"""

import requests
import json


places = ["quán bia", "quán nhậu", "quán bar", "nhà hàng"]
radius = 2000
lat, lng = 21.012985, 105.821839
api = "Has been delete"
N = 50


def get_data(place):
    r = requests.get(
        "https://discover.search.hereapi.com/v1/"
        + "discover"
        + "?in=circle:{},{};r={}".format(lat, lng, radius)
        + "&q={}".format(place)
        + "&apiKey={}".format(api)
    )

    return r.json()


def get_50_places(N, place):
    result = []

    for p in place:
        data = get_data(p)
        result.extend(data["items"])

    return result[:N]


def location(N, place):
    geoMap = {"type": "FeatureCollection", "features": []}

    for data in get_50_places(N, place):
        la = data["position"]["lat"]
        lo = data["position"]["lng"]
        add = data["address"]["label"]
        name = data["title"]
        info = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lo, la]},
            "properties": {"Address": add, "name": name},
        }
        geoMap["features"].append(info)

    return geoMap


def solve(N, place):
    data = location(N, place)
    assert isinstance(data, dict)

    with open("pymi_beer.geojson", "wt", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return


def main():
    n = N
    place = places
    solve(n, place)
    print("Done")
    print(
        "Link to see map: https://github.com/falcol/"
        "BeerAroundPymi/blob/master/pymi_beer.geojson"
    )


if __name__ == "__main__":
    main()
