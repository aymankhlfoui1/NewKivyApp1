[app]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات التطبيق الأساسية ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# اسم التطبيق الظاهر للمستخدمين
title = HTTP Custom Pro

# اسم الحزمة (يجب أن يكون فريدًا، استخدم نظام reverse-domain)
package.name = httpcustom.pro

# نطاق الحزمة (للتطبيقات على Android/iOS)
package.domain = com.httpcustom.pro

# إصدار التطبيق (يُفضَّل استخدام semantic versioning)
version = 1.0.0

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات الملفات والمجلدات ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# المجلد الرئيسي للكود المصدري (حيث يوجد main.py)
source.dir = .

# أنواع الملفات المضمنة في البناء (الامتدادات المسموحة)
source.include_exts = py,png,jpg,kv,ttf,gif,spec

# مجلدات تستبعد من البناء (لتحسين الحجم)
source.exclude_dirs = tests, bin, venv, __pycache__, logs

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات واجهة المستخدم ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# اتجاه الشاشة (portrait/landscape/all)
orientation = portrait

# الأيقونة (يجب أن تكون موجودة في المسار المحدد)
icon.filename = assets/logo.png

# شاشة التحميل الأولية (Presplash)
presplash.filename = assets/loading.gif
presplash.color = #1A1A1A  # لون خلفية Presplash

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ المتطلبات التقنية ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# إصدار بايثون والمكتبات الأساسية
requirements = 
    python3==3.11.6,
    kivy==2.3.0,
    dnspython==2.4.2,
    openssl==23.2.0,
    pyopenssl==23.3.0

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات Android التخصصية ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# صلاحيات النظام المطلوبة
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    FOREGROUND_SERVICE

# إصدارات أدوات التطوير (SDK/NDK)
android.sdk = 34
android.ndk = 25c
android.api = 33

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ التوقيع الرقمي (لتوزيع التطبيق) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# معلومات التوقيع (غيّرها عند النشر الرسمي)
android.release_keystore = user.keystore
android.release_storepassword = 123456
android.release_keyalias = httpcustom
android.release_keypassword = 123456

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات عامة لـ Buildozer ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[buildozer]

# مستوى التفاصيل في السجلات (0 = صامت، 2 = مفصل)
log_level = 2

# تحذير عند التشغيل كـ root (للسلامة)
warn_on_root = 1
