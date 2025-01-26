[app]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات التطبيق الأساسية ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
title = HTTP Custom Pro            # اسم التطبيق الظاهر
package.name = httpcustom_pro      # اسم الحزمة (فريد)
package.domain = com.aymankhifo   # نطاق الحزمة
version = 1.0.0                    # إصدار التطبيق
source.dir = .                     # مجلد الكود المصدري

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات البناء ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
requirements =                     # المتطلبات الأساسية
    python3==3.11.6,
    kivy==2.3.0,
    openssl==23.2.0,
    dnspython==2.4.2,
    pyopenssl==23.3.0,
    requests==2.31.0

android.accept_license = True      # قبول التراخيص تلقائيًا
android.arch = armeabi-v7a         # بنية المعالج

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات Android المتقدمة ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
android.sdk = 34                   # إصدار Android SDK
android.ndk = 25c                  # إصدار Android NDK
android.build_tools = 34.0.0       # إصدار أدوات البناء
android.api = 33                   # إصدار API المستهدف

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ الأذونات والصلاحيات ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
android.permissions =              # صلاحيات النظام
    INTERNET,
    ACCESS_NETWORK_STATE,
    FOREGROUND_SERVICE

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ الأصول والموارد ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
icon.filename = assets/icon.png            # أيقونة التطبيق (512x512 بكسل)
presplash.filename = assets/splash.gif     # شاشة التحميل (800x600 بكسل)
orientation = portrait                     # اتجاه الشاشة

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات التوقيع الرقمي ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
android.release_keystore = user.keystore   # ملف التوقيع
android.release_storepassword = 123456     # كلمة مرور المتجر
android.release_keyalias = httpcustom      # اسم المفتاح
android.release_keypassword = 123456       # كلمة مرور المفتاح

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ إعدادات التخصيص ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
fullscreen = 0                       # عدم استخدام الشاشة الكاملة
log_level = 2                        # مستوى تفصيل السجلات
android.wakelock = False             # منع إبقاء الشاشة مضاءة

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ استثناءات الملفات ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
source.exclude_exts =                # استبعاد امتدادات الملفات
    .pyc,
    .pyo,
    .pyd,
    .git,
    .gitignore

[buildozer]
log_level = 2                        # مستوى تفصيل سجلات البناء
