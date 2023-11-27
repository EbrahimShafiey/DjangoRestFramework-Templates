# DjangoRestFramework-Templates
1. انواع فانکشن بیس ویو ها ، کلاس بیس ویو ها اعم از (mixins, viewsets, generics, ...) ایجاد شد. در همه این کلاس ها، متد های GET,POST,DELETE,PUT ایجاد شد و در دسترس کاربر است.
2. برای هویت سنجی ، از تکنولوژی های (BaseAuthorization, TokenAuthorization, JWT-Authorization) استفاده شد.
3. همچین ارتباط با جداول دیگر (یک به چند و ...) از طریق NestedSerializer ها فراهم شد.
4. اعتبار سنجی مقادیر ورودی در پارامتر ها با استفاده از توابع Validates ایجاد شد.
5. و در آخر با استفاده از ماژول (drf-spectacular) ، ایجاد schema  خودکار توسط swagger انجام شد و در دسترس است.
6. برای مشاهده URL های اصلی به پوشه کانفیگ رفته و برای مشاهده URL  های فرعی به پوشه TODO
