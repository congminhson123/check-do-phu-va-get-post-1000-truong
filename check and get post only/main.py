from API2 import API2
import API1
import time
import pandas as pd
from pandas import DataFrame

if __name__ == "__main__":
    df = pd.read_excel('cellphone 1000 truong.xlsx', converters={'cellphone': str})
    list_phone = []
    for index, row in df.iterrows():
        if row['count field'] != 'error':
            list_phone.append(row['cellphone'])
    print(list_phone)
    field = ['tuổi', 'giới tính', 'tình trạng hôn nhân', 'con cái', 'nghề nghiệp', 'trình độ học vấn', 'ngôn ngữ',
             'quê quán', 'nơi ở hiện tại', 'sở hữu', 'ngân hàng', 'bảo hiểm', 'vay', 'thẻ', 'đầu tư', 'sức khỏe',
             'giáo dục', 'du lịch nước ngoài', 'du lịch trong nước', 'du học', 'thể thao', 'ăn uống',
             'khoa học công nghệ', 'nghệ thuật', 'game', 'sở thích sang', 'xe cộ', 'thời trang', 'nhạc', 'thực phẩm', 'phim', 'làm đẹp']
    do_phu = []
    for i in list_phone:
        start_time = time.time()
        try:
            dictObj = API2().get_all(i)
            API1.user.count += 1
            print(API1.user.count)
            print(API2.is_hometown)

        except:
            continue
        run_time_user = time.time() - start_time
        print(run_time_user)
    do_phu.append(API2.is_age / 3371 * 100)
    do_phu.append(API2.is_gender / 3371 * 100)
    do_phu.append(API2.is_relationship / 3371 * 100)
    do_phu.append(API2.is_child / 3371 * 100)
    do_phu.append(API2.is_job / 3371 * 100)
    do_phu.append(API2.is_edu / 3371 * 100)
    do_phu.append(API2.is_language / 3371 * 100)
    do_phu.append(API2.is_hometown / 3371 * 100)
    do_phu.append(API2.is_location / 3371 * 100)
    do_phu.append(API2.is_own / 3371 * 100)
    do_phu.append(API2.is_nganhang / 3371 * 100)
    do_phu.append(API2.is_baohiem / 3371 * 100)
    do_phu.append(API2.is_vay / 3371 * 100)
    do_phu.append(API2.is_the / 3371 * 100)
    do_phu.append(API2.is_dautu / 3371 * 100)
    do_phu.append(API2.is_suckhoe / 3371 * 100)
    do_phu.append(API2.is_giaoduc / 3371 * 100)
    do_phu.append(API2.is_dulichnuocngoai / 3371 * 100)
    do_phu.append(API2.is_dulichtrongnuoc / 3371 * 100)
    do_phu.append(API2.is_duhoc / 3371 * 100)
    do_phu.append(API2.is_thethao / 3371 * 100)
    do_phu.append(API2.is_anuong / 3371 * 100)
    do_phu.append(API2.is_khoahoc / 3371 * 100)
    do_phu.append(API2.is_nghethuat / 3371 * 100)
    do_phu.append(API2.is_game / 3371 * 100)
    do_phu.append(API2.is_sothichsang / 3371 * 100)
    do_phu.append(API2.is_xeco / 3371 * 100)
    do_phu.append(API2.is_thoitrang / 3371 * 100)
    do_phu.append(API2.is_nhac / 3371 * 100)
    do_phu.append(API2.is_thucpham / 3371 * 100)
    do_phu.append(API2.is_phim / 3371 * 100)
    do_phu.append(API2.is_lamdep / 3371 * 100)
    df = DataFrame({'field': field, 'độ phủ(%)': do_phu})
    df.to_excel(r'check do phu cac truong.xlsx', encoding='utf-8')
