# RuleForge conflict report

These 400 entries were evaluated by the source-priority resolver.
Priority: Blackmatrix, direct over reject, specific host rules, and configured business-category boundaries.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 161
- semantic-overlap: 239
- resolved: 400
- blackmatrix-preferred: 260
- direct-preferred: 7
- specific-preferred: 103
- category-preferred: 30
- unresolved: 0

## reject ↔ china-services

### 1. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 2. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)` (Blackmatrix is the configured primary source.)

### 3. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 4. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 5. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 6. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 7. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 8. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 9. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 10. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 11. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 12. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 13. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 14. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 15. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 20. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

### 21. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 22. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 23. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (Blackmatrix is the configured primary source.)

## reject ↔ china-streaming

### 24. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (Blackmatrix is the configured primary source.)

### 25. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (Blackmatrix is the configured primary source.)

### 26. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (Blackmatrix is the configured primary source.)

### 27. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 28. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 29. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (Blackmatrix is the configured primary source.)

### 30. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (Blackmatrix is the configured primary source.)

## reject ↔ china-direct

### 31. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-blackmatrix` -> `HOST,ad.12306.cn -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 32. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## reject ↔ direct-exception

### 33. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.appsflyer.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,appsflyer.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,app.appsflyer.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 34. semantic-overlap / host-inside-host-suffix
- left: `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,tagtic.cn -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 35. semantic-overlap / host-inside-host-suffix
- left: `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 36. semantic-overlap / host-inside-host-suffix
- left: `HOST,livew.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,livew.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 37. semantic-overlap / host-inside-host-suffix
- left: `HOST,vd.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vd.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 38. semantic-overlap / host-inside-host-suffix
- left: `HOST,vi.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vi.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## reject ↔ google

### 39. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 40. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 41. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 42. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 43. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## reject ↔ microsoft

### 44. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 45. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 46. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 47. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 48. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 49. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 50. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 51. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

## reject ↔ social

### 52. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 53. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)` (Blackmatrix is the configured primary source.)

### 54. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)` (Blackmatrix is the configured primary source.)

## reject ↔ tiktok

### 55. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## reject ↔ youtube

### 56. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## reject ↔ global-media

### 57. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 58. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 59. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)` (Blackmatrix is the configured primary source.)

### 60. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 61. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 62. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 63. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 64. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 65. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 66. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 67. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 68. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

## reject ↔ proxy

### 69. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 70. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 71. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 72. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 73. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 74. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 75. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 76. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 77. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 78. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

## privacy ↔ china-services

### 79. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 80. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 81. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 82. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (Blackmatrix is the configured primary source.)

### 83. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 84. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 85. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 86. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 87. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 88. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

## privacy ↔ china-direct

### 89. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-blackmatrix` -> `HOST,tracking.miui.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## privacy ↔ direct-exception

### 90. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.adjust.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,adjust.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,app.adjust.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## privacy ↔ ai

### 91. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 92. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-copilot)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

## privacy ↔ google

### 93. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 94. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 95. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## privacy ↔ microsoft

### 96. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

## privacy ↔ social

### 97. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)` (Blackmatrix is the configured primary source.)

### 98. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)` (Blackmatrix is the configured primary source.)

## privacy ↔ global-media

### 99. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

## privacy ↔ proxy

### 100. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (A specific host rule takes precedence over a broader host rule.)

## china-services ↔ proxy

### 101. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

### 102. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)` (Blackmatrix is the configured primary source.)

## china-streaming ↔ china-media

### 103. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 104. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 105. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 106. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 107. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 108. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 109. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 110. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 111. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 112. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 113. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

## china-streaming ↔ global-media

### 114. exact-policy / same-rule-different-policy
- left: `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 115. exact-policy / same-rule-different-policy
- left: `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 116. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 117. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 118. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)`
- right: `HOST-SUFFIX,bilibili.tv -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)` (The configured business-category priority applies to this conflict.)

### 119. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 120. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 121. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 122. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,110.238.107.47/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 123. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 124. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 125. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.202/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 126. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 127. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 128. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 129. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 130. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 131. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 132. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 133. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 134. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 135. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 136. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 137. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 138. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (A specific host rule takes precedence over a broader host rule.)

### 139. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 140. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 141. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 143. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (A specific host rule takes precedence over a broader host rule.)

### 148. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (A specific host rule takes precedence over a broader host rule.)

### 149. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (A specific host rule takes precedence over a broader host rule.)

### 150. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (A specific host rule takes precedence over a broader host rule.)

### 151. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (A specific host rule takes precedence over a broader host rule.)

## china-direct ↔ apple

### 152. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this conflict.)

### 153. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ google

### 154. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 155. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 156. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 157. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 158. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 159. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 160. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 161. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 162. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 163. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 164. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

## china-direct ↔ proxy

### 165. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ google

### 166. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 167. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 168. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 169. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 170. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 171. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 172. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 173. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ youtube

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ proxy

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A specific host rule takes precedence over a broader host rule.)

## ai ↔ apple

### 177. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source.)

### 178. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

## ai ↔ google

### 180. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 183. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 184. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 185. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 186. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 187. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 188. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 189. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 190. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 191. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 192. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 193. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 194. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 195. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 196. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 197. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

## ai ↔ microsoft

### 198. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)` (A specific host rule takes precedence over a broader host rule.)

### 199. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)` (A specific host rule takes precedence over a broader host rule.)

### 200. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)` (A specific host rule takes precedence over a broader host rule.)

### 201. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 202. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 203. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 204. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 205. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 206. semantic-overlap / host-inside-host-suffix
- left: `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,appcenter.ms -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 207. semantic-overlap / host-inside-host-suffix
- left: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 208. semantic-overlap / host-inside-host-suffix
- left: `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,live.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 209. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 210. semantic-overlap / host-inside-host-suffix
- left: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 211. semantic-overlap / host-inside-host-suffix
- left: `HOST,services.bingapis.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bingapis.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,services.bingapis.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 212. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 213. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 214. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 215. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 216. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 217. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)` (A specific host rule takes precedence over a broader host rule.)

### 218. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 219. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (A specific host rule takes precedence over a broader host rule.)

### 220. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 221. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

## ai ↔ social

### 222. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 223. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)` (Blackmatrix is the configured primary source.)

## ai ↔ developer

### 224. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 225. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 226. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

## ai ↔ github

### 227. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 228. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 229. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

## ai ↔ global-media

### 230. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney.my.sentry.io -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,sentry.io -> AI (blackmatrix-openai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,disney.my.sentry.io -> 国际媒体 (blackmatrix-global-media-disney)` (A specific host rule takes precedence over a broader host rule.)

## ai ↔ proxy

### 231. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)`
- right: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)` (Blackmatrix is the configured primary source.)

### 232. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 233. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 234. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 235. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 236. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 237. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 238. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 239. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 240. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 241. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 242. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 243. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 244. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (A specific host rule takes precedence over a broader host rule.)

### 245. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A specific host rule takes precedence over a broader host rule.)

### 246. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A specific host rule takes precedence over a broader host rule.)

## apple ↔ global-media

### 247. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 248. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 249. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 250. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 251. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 252. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

## apple ↔ proxy

### 253. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 254. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 255. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 256. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 257. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)` (Blackmatrix is the configured primary source.)

### 258. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 259. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 260. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 261. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 262. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source.)

### 263. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 264. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 265. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 266. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 267. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 268. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 269. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 270. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 271. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

### 272. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source.)

### 273. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)` (Blackmatrix is the configured primary source.)

### 274. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source.)

## google-voice ↔ google

### 275. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (A specific host rule takes precedence over a broader host rule.)

## google ↔ social

### 276. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (A specific host rule takes precedence over a broader host rule.)

### 277. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)` (A specific host rule takes precedence over a broader host rule.)

## google ↔ youtube

### 278. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 279. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 280. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 281. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 282. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 283. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 284. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 285. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 286. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 287. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 288. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 289. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 290. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 291. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 292. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 293. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 294. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

## google ↔ global-media

### 295. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## google ↔ proxy

### 296. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 297. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 298. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 299. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 300. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 301. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 302. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 303. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 304. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 305. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 306. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 307. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 308. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## microsoft ↔ spotify

### 309. semantic-overlap / host-inside-host-suffix
- left: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (A specific host rule takes precedence over a broader host rule.)

## microsoft ↔ netflix

### 310. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A specific host rule takes precedence over a broader host rule.)

### 311. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A specific host rule takes precedence over a broader host rule.)

## microsoft ↔ global-media

### 312. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)` (A specific host rule takes precedence over a broader host rule.)

### 313. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)` (A specific host rule takes precedence over a broader host rule.)

### 314. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)` (A specific host rule takes precedence over a broader host rule.)

### 315. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)`
- decision: `prefer-specific` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)` (A specific host rule takes precedence over a broader host rule.)

## developer ↔ github

### 316. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npm.community -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 317. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 318. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.org -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

## developer ↔ global-media

### 319. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (blackmatrix-global-media-abema-tv)`
- decision: `prefer-specific` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)` (A specific host rule takes precedence over a broader host rule.)

## github ↔ proxy

### 320. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 321. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 322. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 323. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 324. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 325. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 326. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

## spotify ↔ global-media

### 327. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 328. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 329. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 330. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

## telegram ↔ proxy

### 331. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 332. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 333. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 334. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 335. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 336. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 337. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 338. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 339. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 340. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 341. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 342. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 343. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 344. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 345. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 346. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

## tiktok ↔ global-media

### 347. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 348. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 349. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 350. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 351. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 352. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 353. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 354. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## youtube ↔ global-media

### 355. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 356. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 357. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 358. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 359. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 360. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 361. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 362. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 363. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 364. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 365. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 366. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 367. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)` (Blackmatrix is the configured primary source.)

## youtube ↔ proxy

### 368. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## netflix ↔ global-media

### 369. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 370. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 371. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 372. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 373. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 374. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 375. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 376. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 377. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 378. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 379. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 380. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,onetrust.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)` (A specific host rule takes precedence over a broader host rule.)

## china-media ↔ global-media

### 381. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-blackmatrix` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Blackmatrix is the configured primary source.)

### 382. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 383. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 384. exact-policy / same-rule-different-policy
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 385. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 386. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 387. exact-policy / same-rule-different-policy
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 388. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 389. exact-policy / same-rule-different-policy
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 390. exact-policy / same-rule-different-policy
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 391. exact-policy / same-rule-different-policy
- left: `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 392. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 393. exact-policy / same-rule-different-policy
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 394. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

### 395. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)` (Blackmatrix is the configured primary source.)

## global-media ↔ proxy

### 396. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 397. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 398. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)` (Blackmatrix is the configured primary source.)

### 399. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 400. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (A specific host rule takes precedence over a broader host rule.)
