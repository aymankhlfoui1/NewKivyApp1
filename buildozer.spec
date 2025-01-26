[app]

# عنوان التطبيق
title = NewKivyApp1

# اسم الحزمة (يجب أن يكون فريدًا)
package.name = com.aymankhifou.newkivyapp1

# اسم المجلد الرئيسي للتطبيق (حيث يوجد main.py)
source.dir = .

# ملف التشغيل الرئيسي
source.include_exts = py,png,jpg,kv,ttf

# إصدار التطبيق
version = 1.0

# القواعد المطلوبة (Kivy هنا)
requirements = 
    python3,
    kivy==2.1.0,
    android,
    openssl,
    requests

# إصدار Android SDK المستهدف
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.gradle_download = True

# إعدادات البناء
android.accept_sdk_license = True  # ⭐ قبول التراخيص تلقائيًا
android.release_artifact = .apk
p4a.branch = develop

# إعدادات الأذونات (عدلها حسب حاجة التطبيق)
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE

# إعدادات OpenSSL (مهمة للاتصال الآمن)
android.openssl_static = True

# إعدادات الأيقونة والشاشة التمهيدية
icon.filename = %(source.dir)s/data/images/icon.png
presplash.filename = %(source.dir)s/data/images/presplash.png

# إعدادات الأداء
fullscreen = 0
orientation = portrait

# إعدادات التوقيع (اتركها فارغة للبناء للتجربة)
# (للبناء النهائي، أضف مفاتيح التوقيع هنا)
# android.keystore = 
# android.keystore_passwd = 
# android.keyalias = 
# android.keyalias_passwd = 

[buildozer]
# إصدار Buildozer
log_level = 2
warn_on_root = 1
