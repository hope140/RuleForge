# RuleForge conflict report

These 930 entries were evaluated by the source-priority resolver.
Priority: Blackmatrix, direct over reject, specific host rules, and configured business-category boundaries.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 175
- semantic-overlap: 755
- resolved: 930
- blackmatrix-preferred: 135
- direct-preferred: 63
- specific-preferred: 463
- category-preferred: 208
- protective-reject: 61
- unresolved: 0

## reject ↔ china-services

### 1. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 2. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)`
- decision: `prefer-direct` -> `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)` (direct takes precedence over reject.)

### 3. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 4. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 5. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 6. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 7. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 8. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 9. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 10. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 11. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 12. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 13. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 14. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 15. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 20. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 21. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 22. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 23. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 24. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 25. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 26. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 27. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 28. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

## reject ↔ china-streaming

### 29. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 30. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 31. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 32. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 33. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 34. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 35. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 36. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 37. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 38. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 39. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

## reject ↔ china-direct

### 40. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST,ad.12306.cn -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 41. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 42. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 43. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

## reject ↔ direct-exception

### 44. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.appsflyer.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,appsflyer.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,app.appsflyer.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 45. semantic-overlap / host-inside-host-suffix
- left: `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,tagtic.cn -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 46. semantic-overlap / host-inside-host-suffix
- left: `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 47. semantic-overlap / host-inside-host-suffix
- left: `HOST,livew.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,livew.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 48. semantic-overlap / host-inside-host-suffix
- left: `HOST,vd.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vd.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 49. semantic-overlap / host-inside-host-suffix
- left: `HOST,vi.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vi.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 50. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-direct` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 51. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-direct` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## reject ↔ google

### 52. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 53. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 54. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 55. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 56. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 57. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 58. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 59. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 60. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 61. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 62. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 63. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 64. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ microsoft

### 65. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 66. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 67. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 68. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 69. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 70. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 71. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 72. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 73. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ social

### 74. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 75. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 76. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 77. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,twitter -> 全球加速 (blackmatrix-social-twitter)`
- right: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ tiktok

### 78. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-reject` -> `HOST,pangolin.snssdk.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ youtube

### 79. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 80. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ global-media

### 81. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 82. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 83. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)`
- decision: `prefer-reject` -> `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 84. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 85. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 86. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 87. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 88. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 89. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 90. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 91. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 92. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ proxy

### 93. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 94. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 95. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 96. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 97. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 98. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 99. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 100. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 101. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 102. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 103. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 104. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 105. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 106. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 107. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,.pinterest -> 全球加速 (rulego-proxy)`
- right: `HOST,ads.pinterest.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST,ads.pinterest.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ china-services

### 108. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 109. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 110. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 111. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 112. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 113. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 114. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 115. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 116. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 117. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

## privacy ↔ china-direct

### 118. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,tracking.miui.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

## privacy ↔ direct-exception

### 119. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.adjust.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,adjust.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,app.adjust.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## privacy ↔ ai

### 120. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

## privacy ↔ google

### 121. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 122. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 123. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 124. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 125. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 126. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ microsoft

### 127. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST,c.bing.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ social

### 128. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 129. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ global-media

### 130. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ proxy

### 131. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 133. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 134. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## china-services ↔ google

### 135. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)` (A more specific rule takes precedence over a broader overlap.)

### 136. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)` (A more specific rule takes precedence over a broader overlap.)

## china-services ↔ proxy

### 137. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-specific` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 138. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-specific` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

## china-streaming ↔ china-media

### 139. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 140. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 141. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 143. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 148. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 149. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 150. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

## china-streaming ↔ global-media

### 151. exact-policy / same-rule-different-policy
- left: `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 152. exact-policy / same-rule-different-policy
- left: `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 153. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 154. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 155. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)`
- right: `HOST-SUFFIX,bilibili.tv -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)` (The configured business-category priority applies to this conflict.)

### 156. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 157. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 158. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 159. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 160. exact-policy / same-rule-different-policy
- left: `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 161. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 162. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 163. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 164. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 165. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 166. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 167. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 168. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 169. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 170. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 171. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 172. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 173. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 174. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 175. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 176. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 180. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 183. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 184. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 185. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 186. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 187. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 188. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 189. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 190. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 191. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 192. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 193. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 194. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 195. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 196. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 197. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 198. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 199. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 200. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 201. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 202. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 203. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 204. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 205. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 206. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 207. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 208. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 209. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 210. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 211. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 212. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ ai

### 213. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 214. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

## china-direct ↔ apple

### 215. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this conflict.)

### 216. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 217. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 218. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 219. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 220. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gsa.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)`
- decision: `prefer-category` -> `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)` (The configured business-category priority applies to this conflict.)

### 221. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)`
- decision: `prefer-category` -> `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)` (The configured business-category priority applies to this conflict.)

### 222. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-category` -> `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this conflict.)

### 223. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-category` -> `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this conflict.)

### 224. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-category` -> `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this conflict.)

### 225. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- decision: `prefer-category` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ google

### 226. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 227. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 228. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 229. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 230. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 231. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 232. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 233. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 234. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 235. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 236. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 237. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 238. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 239. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 240. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 241. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 242. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 243. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ global-media

### 244. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)`
- decision: `prefer-category` -> `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ proxy

### 245. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 246. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 247. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,amp-api.podcasts.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 248. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 249. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 250. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 251. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 252. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 253. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 254. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 255. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 256. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 257. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ google

### 258. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 259. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 260. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 261. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,ci.android.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 262. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 263. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 264. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 265. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 266. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 267. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 268. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 269. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 270. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 271. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 272. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 273. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ youtube

### 274. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ proxy

### 275. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 276. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 277. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 278. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 279. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 280. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 281. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 282. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ apple

### 283. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source.)

### 284. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ google

### 285. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 286. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 287. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 288. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 289. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 290. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 291. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 292. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 293. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 294. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 295. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 296. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 297. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 298. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 299. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 300. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 301. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 302. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 303. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 304. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 305. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 306. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 307. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 308. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 309. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 310. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 311. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 312. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 313. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 314. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 315. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 316. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 317. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 318. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 319. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 320. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 321. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 322. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 323. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 324. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 325. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

## ai ↔ microsoft

### 326. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 327. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 328. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 329. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 330. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 331. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 332. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 333. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 334. semantic-overlap / host-inside-host-suffix
- left: `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,appcenter.ms -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 335. semantic-overlap / host-inside-host-suffix
- left: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 336. semantic-overlap / host-inside-host-suffix
- left: `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,live.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 337. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 338. semantic-overlap / host-inside-host-suffix
- left: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 339. semantic-overlap / host-inside-host-suffix
- left: `HOST,services.bingapis.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bingapis.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,services.bingapis.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 340. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 341. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 342. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 343. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 344. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 345. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 346. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 347. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 348. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 349. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 350. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 351. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 352. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 353. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 354. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 355. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 356. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 357. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 358. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ social

### 359. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 360. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)`
- decision: `prefer-specific` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ developer

### 361. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 362. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 363. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-specific` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ github

### 364. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 365. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-specific` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 366. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 367. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 368. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 369. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ tiktok

### 370. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## ai ↔ global-media

### 371. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 372. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney.my.sentry.io -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,sentry.io -> AI (blackmatrix-openai)`
- decision: `prefer-category` -> `HOST-SUFFIX,sentry.io -> AI (blackmatrix-openai)` (The configured business-category priority applies to this conflict.)

## ai ↔ proxy

### 373. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)`
- right: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)` (Blackmatrix is the configured primary source.)

### 374. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 375. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 376. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 377. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 378. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 379. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 380. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 381. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 382. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 383. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 384. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 385. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 386. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 387. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 388. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,openai -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 389. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 390. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 391. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 392. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 393. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 394. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 395. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 396. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 397. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 398. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 399. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 400. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 401. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 402. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 403. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 404. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 405. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 406. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 407. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 408. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 409. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 410. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 411. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## apple ↔ global-media

### 412. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 413. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 414. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 415. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 416. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 417. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

## apple ↔ proxy

### 418. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 419. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 420. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 421. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 422. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)` (Blackmatrix is the configured primary source.)

### 423. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 424. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 425. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 426. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 427. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source.)

### 428. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 429. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 430. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 431. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 432. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 433. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 434. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 435. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 436. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 437. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-specific` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 438. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)`
- decision: `prefer-specific` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 439. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 440. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,testflight -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

## google-voice ↔ google

### 441. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this conflict.)

### 442. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this conflict.)

## google-voice ↔ proxy

### 443. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `prefer-specific` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (A more specific rule takes precedence over a broader overlap.)

## google ↔ social

### 444. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

### 445. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

### 446. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- decision: `prefer-category` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

## google ↔ youtube

### 447. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 448. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 449. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 450. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 451. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 452. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 453. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 454. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 455. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 456. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 457. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 458. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 459. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 460. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 461. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 462. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 463. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 464. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 465. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 466. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 467. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 468. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 469. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 470. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

## google ↔ global-media

### 471. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 472. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 473. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

## google ↔ proxy

### 474. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 475. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 476. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 477. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 478. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 479. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 480. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 481. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 482. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 483. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 484. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 485. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 486. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 487. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,appspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 488. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,blogspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 489. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 490. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 491. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 492. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 493. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 494. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 495. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 496. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 497. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 498. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 499. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 500. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 501. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 502. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 503. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 504. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 505. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 506. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 507. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 508. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 509. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 510. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 511. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 512. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 513. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 514. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 515. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 516. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 517. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 518. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 519. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 520. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 521. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 522. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 523. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 524. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 525. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 526. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 527. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 528. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 529. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 530. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 531. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 532. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 533. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 534. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 535. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 536. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 537. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 538. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 539. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 540. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 541. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 542. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 543. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 544. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 545. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 546. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 547. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 548. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 549. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 550. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 551. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 552. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 553. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 554. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 555. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 556. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 557. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 558. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 559. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 560. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 561. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 562. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 563. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 564. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 565. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 566. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 567. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 568. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 569. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 570. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 571. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 572. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 573. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 574. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 575. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 576. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 577. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 578. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 579. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 580. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 581. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 582. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 583. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 584. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 585. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 586. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 587. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 588. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 589. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 590. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 591. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 592. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 593. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 594. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 595. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 596. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 597. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 598. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 599. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 600. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 601. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 602. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 603. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 604. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 605. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 606. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 607. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 608. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 609. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 610. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 611. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 612. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 613. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 614. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 615. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 616. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 617. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 618. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 619. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 620. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 621. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 622. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 623. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 624. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 625. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 628. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 629. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 631. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 632. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 633. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 634. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 635. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 636. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 637. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 638. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 639. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 640. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 641. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 642. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 643. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 644. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 645. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 646. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 647. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 648. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 649. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 650. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 651. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 652. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 653. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 654. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 655. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 656. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 657. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 658. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 659. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 660. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 661. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 662. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 663. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 664. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 665. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 666. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 667. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 668. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 669. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 670. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 671. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 672. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 673. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 674. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 675. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 676. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 677. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 678. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 679. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 680. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 681. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 682. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 683. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 684. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 686. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 691. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 692. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 693. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 694. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 695. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 696. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 697. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 698. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 699. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 700. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 701. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 702. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 703. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 704. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 705. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 706. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 707. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 708. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 709. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 710. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 711. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 712. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 713. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 714. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 715. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 716. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 717. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 718. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 719. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 720. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 721. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 722. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 723. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 729. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 730. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 731. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 732. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 733. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 734. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 735. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 736. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 737. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 738. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 739. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 740. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 741. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 742. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 743. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 744. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 745. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 746. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 747. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 748. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 749. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 750. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 751. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `prefer-specific` -> `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google-drive)` (A more specific rule takes precedence over a broader overlap.)

### 752. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `prefer-specific` -> `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)` (A more specific rule takes precedence over a broader overlap.)

### 753. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `prefer-specific` -> `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)` (A more specific rule takes precedence over a broader overlap.)

### 754. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 755. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 756. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 757. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 758. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 765. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 766. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 767. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 768. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 769. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ spotify

### 770. semantic-overlap / host-inside-host-suffix
- left: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ netflix

### 771. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 772. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ global-media

### 773. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)` (A more specific rule takes precedence over a broader overlap.)

### 774. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 775. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 776. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)`
- decision: `prefer-specific` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)` (A more specific rule takes precedence over a broader overlap.)

## developer ↔ github

### 777. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npm.community -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 778. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 779. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.org -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

## developer ↔ global-media

### 780. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (blackmatrix-global-media-abema-tv)`
- decision: `prefer-specific` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)` (A more specific rule takes precedence over a broader overlap.)

## github ↔ proxy

### 781. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 782. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 783. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 784. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 785. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 786. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 787. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 788. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 789. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 790. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 791. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 792. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 793. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,github.global.ssl.fastly.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

## spotify ↔ global-media

### 794. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 795. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 796. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 797. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 798. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 799. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 800. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 801. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 802. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 803. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 804. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 805. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 806. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 807. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 808. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

## telegram ↔ proxy

### 809. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 810. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 811. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 812. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 813. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 814. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 815. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 816. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 817. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 818. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 819. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 820. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 821. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 822. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 823. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 824. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 825. exact-policy / same-rule-different-policy
- left: `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 826. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23f::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 827. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:67c:4e8::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 828. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 829. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 830. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 831. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 832. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 833. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 834. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 835. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 836. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

## tiktok ↔ global-media

### 837. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 838. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 839. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 840. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 841. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 842. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 843. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 844. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 845. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 846. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 847. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 848. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 849. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 850. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 851. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-category` -> `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 852. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

## youtube ↔ global-media

### 853. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 854. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 855. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 856. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 857. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 858. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 859. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 860. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 861. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 862. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 863. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 864. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 865. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)` (The configured business-category priority applies to this conflict.)

### 866. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 867. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 868. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 869. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 870. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 871. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 872. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

## youtube ↔ proxy

### 873. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 874. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 875. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 876. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 877. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 878. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 879. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 880. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

## netflix ↔ global-media

### 881. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 882. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 883. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 884. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 885. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 886. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 887. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 888. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 889. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 890. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 891. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 892. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,onetrust.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 893. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 894. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 895. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 896. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 897. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 898. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 899. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 900. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 901. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 902. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 903. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 904. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 905. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 906. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

## china-media ↔ global-media

### 907. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 908. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 909. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 910. exact-policy / same-rule-different-policy
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 911. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 912. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 913. exact-policy / same-rule-different-policy
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 914. exact-policy / same-rule-different-policy
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 915. exact-policy / same-rule-different-policy
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 916. exact-policy / same-rule-different-policy
- left: `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 917. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 918. exact-policy / same-rule-different-policy
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 919. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 920. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 921. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.206/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 922. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.216/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

## global-media ↔ proxy

### 924. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 925. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 926. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)` (Blackmatrix is the configured primary source.)

### 927. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 928. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 929. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 930. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)
