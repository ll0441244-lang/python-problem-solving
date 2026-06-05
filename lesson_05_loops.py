# وضع قائمة لتخزين الخدمات
my_services = ["Web Scraping", "Automation", "Data Analysis"]

print("---------- my services ----------")

# نستخدم enumerate ليعطينا الرقم (i) والخدمة (service) معاً
# بدأنا العد من 1 (start=1) لكي لا يبدأ بايثون من الصفر
for i, service in enumerate(my_services, start=1):
    print(i, "-", service)

print("---------------------------------")
