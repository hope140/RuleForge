# RuleForge conflict report

These 1139 entries were evaluated by the source-priority resolver.
Priority: Blackmatrix, direct over reject, specific host rules, and configured business-category boundaries.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 194
- semantic-overlap: 945
- resolved: 1139
- blackmatrix-preferred: 146
- direct-preferred: 87
- specific-preferred: 569
- category-preferred: 273
- protective-reject: 64
- unresolved: 0

## reject ↔ china-services

### 1. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tanx.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tanx.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,tanx.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 2. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yukhj.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yukhj.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,yukhj.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 3. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 4. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)`
- decision: `prefer-direct` -> `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)` (direct takes precedence over reject.)

### 5. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 6. semantic-overlap / host-inside-host-suffix
- left: `HOST,hc-ssp.sm.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sm.cn -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sm.cn -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 7. semantic-overlap / host-inside-host-suffix
- left: `HOST,tunion-api.m.taobao.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,taobao.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,taobao.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 8. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,amap.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,amap.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 9. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com.w.alikunlun.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,alikunlun.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,alikunlun.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 10. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 11. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 12. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 13. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 14. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 15. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstore-index-1252524079.file.myqcloud.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,myqcloud.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,myqcloud.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 20. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 21. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 22. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 23. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 24. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 25. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 26. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 27. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 28. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.gdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gdtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 29. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 30. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 31. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.cn -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gtimg.cn -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 32. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 33. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 34. semantic-overlap / host-inside-host-suffix
- left: `HOST,splashqqlive.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 35. semantic-overlap / host-inside-host-suffix
- left: `HOST,wa.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 36. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 37. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 38. semantic-overlap / host-inside-host-suffix
- left: `HOST,tmead.y.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 39. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adchina.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,afp.adchina.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-direct` -> `HOST-SUFFIX,afp.adchina.com -> direct (blackmatrix-china-services-alibaba)` (direct takes precedence over reject.)

### 40. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 41. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 42. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 43. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-direct` -> `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 44. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 45. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 46. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 47. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 48. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 49. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 50. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

### 51. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)` (direct takes precedence over reject.)

## reject ↔ china-streaming

### 52. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 53. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 54. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 55. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 56. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 57. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 58. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `prefer-direct` -> `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)` (direct takes precedence over reject.)

### 59. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 60. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 61. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

### 62. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-direct` -> `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)` (direct takes precedence over reject.)

## reject ↔ china-direct

### 63. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST,ad.12306.cn -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 64. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 65. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-direct` -> `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

### 66. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

## reject ↔ direct-exception

### 67. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.appsflyer.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,appsflyer.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,app.appsflyer.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 68. semantic-overlap / host-inside-host-suffix
- left: `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,tagtic.cn -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 69. semantic-overlap / host-inside-host-suffix
- left: `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 70. semantic-overlap / host-inside-host-suffix
- left: `HOST,livew.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,livew.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 71. semantic-overlap / host-inside-host-suffix
- left: `HOST,vd.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vd.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 72. semantic-overlap / host-inside-host-suffix
- left: `HOST,vi.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vi.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 73. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-direct` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 74. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-direct` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## reject ↔ apple

### 75. semantic-overlap / host-inside-host-suffix
- left: `HOST,iadsdk.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 76. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ google

### 77. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 78. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 79. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 80. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 81. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 82. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 83. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 84. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 85. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 86. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 87. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 88. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 89. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ microsoft

### 90. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 91. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)` (Blackmatrix is the configured primary source.)

### 92. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 93. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 94. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 95. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 96. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 97. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 98. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ social

### 99. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 100. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 101. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 102. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,twitter -> 全球加速 (blackmatrix-social-twitter)`
- right: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ tiktok

### 103. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-reject` -> `HOST,pangolin.snssdk.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ youtube

### 104. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 105. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ global-media

### 106. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 107. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 108. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)`
- decision: `prefer-reject` -> `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 109. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 110. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-reject` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 111. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 112. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 113. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 114. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 115. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 116. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 117. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## reject ↔ proxy

### 118. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 119. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 120. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 121. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 122. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 123. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 124. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 125. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 126. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 127. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 128. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 129. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 130. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 131. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

### 132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,.pinterest -> 全球加速 (rulego-proxy)`
- right: `HOST,ads.pinterest.com -> reject (rulego-advertising)`
- decision: `prefer-reject` -> `HOST,ads.pinterest.com -> reject (rulego-advertising)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ china-services

### 133. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 134. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 135. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 136. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-direct` -> `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)` (direct takes precedence over reject.)

### 137. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 138. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 139. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 140. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 141. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-direct` -> `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.urlsec.qq.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-direct` -> `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)` (direct takes precedence over reject.)

### 143. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)` (direct takes precedence over reject.)

## privacy ↔ china-direct

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,tracking.miui.com -> direct (blackmatrix-direct)` (direct takes precedence over reject.)

## privacy ↔ direct-exception

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.adjust.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,adjust.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,app.adjust.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## privacy ↔ ai

### 146. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

## privacy ↔ apple

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,token.safebrowsing.apple -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,safebrowsing.apple -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-reject` -> `HOST,token.safebrowsing.apple -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ google

### 148. exact-policy / same-rule-different-policy
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 149. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 150. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 151. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 152. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 153. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 154. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ microsoft

### 155. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST,c.bing.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ social

### 156. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 157. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `prefer-reject` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ global-media

### 158. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## privacy ↔ proxy

### 159. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 160. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 161. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

### 162. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Reject rules protect against a broader semantic overlap.)

## china-services ↔ apple

### 163. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,autonavi.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,dispatcher.is.autonavi.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST-SUFFIX,dispatcher.is.autonavi.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

## china-services ↔ google

### 164. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)` (A more specific rule takes precedence over a broader overlap.)

### 165. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)` (A more specific rule takes precedence over a broader overlap.)

## china-services ↔ developer

### 166. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (blackmatrix-developer-gitlab)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (blackmatrix-developer-gitlab)` (A more specific rule takes precedence over a broader overlap.)

## china-services ↔ github

### 167. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (blackmatrix-github)`
- decision: `prefer-specific` -> `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (blackmatrix-github)` (A more specific rule takes precedence over a broader overlap.)

## china-services ↔ global-media

### 168. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,joox.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,joox.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,joox.com -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source.)

### 169. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,wetv.vip -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,wetv.vip -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,wetv.vip -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source.)

### 170. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,wetvinfo.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,wetvinfo.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,wetvinfo.com -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source.)

## china-services ↔ proxy

### 171. semantic-overlap / host-inside-host-suffix
- left: `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-specific` -> `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 172. semantic-overlap / host-inside-host-suffix
- left: `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-specific` -> `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 173. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-specific` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `prefer-specific` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

## china-streaming ↔ china-media

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 180. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 183. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 184. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-specific` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 185. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

### 186. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- decision: `prefer-specific` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (A more specific rule takes precedence over a broader overlap.)

## china-streaming ↔ global-media

### 187. exact-policy / same-rule-different-policy
- left: `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 188. exact-policy / same-rule-different-policy
- left: `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 189. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 190. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 191. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)`
- right: `HOST-SUFFIX,bilibili.tv -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)` (The configured business-category priority applies to this conflict.)

### 192. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)` (Blackmatrix is the configured primary source.)

### 193. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 194. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 195. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 196. exact-policy / same-rule-different-policy
- left: `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 197. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 198. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 199. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 200. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 201. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 202. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 203. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 204. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 205. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 206. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 207. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 208. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 209. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 210. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 211. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 212. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)` (Blackmatrix is the configured primary source.)

### 213. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 214. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 215. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 216. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 217. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 218. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 219. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 220. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 221. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 222. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 223. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 224. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 225. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 226. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 227. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 228. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 229. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 230. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 231. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 232. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 233. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 234. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 235. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 236. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 237. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 238. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 239. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 240. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 241. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 242. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 243. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 244. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 245. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this conflict.)

### 246. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 247. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

### 248. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ ai

### 249. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 250. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

## china-direct ↔ apple

### 251. exact-policy / same-rule-different-policy
- left: `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 252. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 253. exact-policy / same-rule-different-policy
- left: `HOST,smp-device-content.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,smp-device-content.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 254. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 255. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 256. semantic-overlap / host-inside-host-suffix
- left: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 257. semantic-overlap / host-inside-host-suffix
- left: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 258. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 259. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 260. semantic-overlap / host-inside-host-suffix
- left: `HOST,time.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 261. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-analytics-events.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 262. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 263. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 264. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 265. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 266. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 267. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,api.smoot.apple.cn -> direct (blackmatrix-direct)`
- right: `HOST,api.smoot.apple.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,api.smoot.apple.cn -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 268. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 269. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.fitness.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,amp-api.fitness.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 270. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gsa.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)`
- decision: `prefer-category` -> `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)` (The configured business-category priority applies to this conflict.)

### 271. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 272. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 273. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 274. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 275. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 276. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,fmfmobile.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,fmfmobile.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 277. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,fmipmobile.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,fmipmobile.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 278. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,statici.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,statici.icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 279. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 280. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,applemx-icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,applemx-icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 281. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 282. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,icloud.com.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,icloud.com.cn -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 283. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,ios-icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,ios-icloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 284. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,wwwicloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,wwwicloud.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 285. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-WILDCARD,*-content.icloud.com.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-WILDCARD,*-content.icloud.com.cn -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 286. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)`
- decision: `prefer-category` -> `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)` (The configured business-category priority applies to this conflict.)

### 287. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp10-ssl-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp10-ssl-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 288. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp12-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp12-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 289. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp13-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp13-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 290. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp4-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 291. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 292. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 293. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp5-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp5-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 294. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gsp85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 295. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe11-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe11-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 296. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe12-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe12-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 297. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe19-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 298. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe19-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 299. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe19-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 300. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe21-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe21-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 301. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe21.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe21.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 302. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe35-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe35-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 303. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe79-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe79-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 304. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 305. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 306. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 307. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 308. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init-p01st.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,init-p01st.push.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 309. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init-s01st.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST,init-s01st.push.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

### 310. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-WILDCARD,init*.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-category` -> `HOST-WILDCARD,init*.push.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ google

### 311. exact-policy / same-rule-different-policy
- left: `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 312. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 313. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 314. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 315. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 316. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 317. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 318. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 319. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 320. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 321. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 322. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 323. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 324. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 325. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 326. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 327. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 328. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

### 329. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ global-media

### 330. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)`
- decision: `prefer-category` -> `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)` (The configured business-category priority applies to this conflict.)

## china-direct ↔ proxy

### 331. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 332. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 333. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,amp-api.podcasts.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 334. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 335. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 336. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 337. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 338. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 339. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 340. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 341. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 342. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

### 343. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ google

### 344. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 345. exact-policy / same-rule-different-policy
- left: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 346. exact-policy / same-rule-different-policy
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 347. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 348. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 349. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 350. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 351. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,ci.android.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 352. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 353. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 354. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 355. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 356. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 357. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 358. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 359. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 360. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 361. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ youtube

### 362. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## direct-exception ↔ proxy

### 363. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 364. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 365. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 366. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 367. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 368. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 369. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

### 370. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ apple

### 371. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 372. exact-policy / same-rule-different-policy
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 373. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 374. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 375. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 376. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 377. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 378. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 379. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 380. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 381. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 382. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 383. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 384. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 385. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ google

### 386. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 387. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 388. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 389. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 390. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 391. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 392. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 393. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 394. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 395. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 396. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 397. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 398. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 399. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 400. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 401. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 402. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 403. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 404. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 405. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 406. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 407. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 408. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 409. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 410. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 411. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 412. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 413. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 414. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-category` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this conflict.)

### 415. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 416. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 417. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 418. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 419. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 420. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 421. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 422. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-category` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 423. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 424. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 425. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

### 426. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (The configured business-category priority applies to this conflict.)

## ai ↔ microsoft

### 427. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 428. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 429. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 430. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 431. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 432. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 433. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 434. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 435. semantic-overlap / host-inside-host-suffix
- left: `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,appcenter.ms -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 436. semantic-overlap / host-inside-host-suffix
- left: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 437. semantic-overlap / host-inside-host-suffix
- left: `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,live.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 438. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 439. semantic-overlap / host-inside-host-suffix
- left: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 440. semantic-overlap / host-inside-host-suffix
- left: `HOST,services.bingapis.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bingapis.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,services.bingapis.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 441. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 442. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 443. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 444. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 445. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 446. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)` (A more specific rule takes precedence over a broader overlap.)

### 447. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 448. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 449. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 450. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 451. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 452. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 453. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 454. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 455. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 456. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 457. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (A more specific rule takes precedence over a broader overlap.)

### 458. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 459. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ social

### 460. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source.)

### 461. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)`
- decision: `prefer-specific` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ developer

### 462. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 463. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source.)

### 464. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-specific` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ github

### 465. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 466. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-specific` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 467. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 468. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 469. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 470. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## ai ↔ tiktok

### 471. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## ai ↔ global-media

### 472. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 473. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney.my.sentry.io -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,sentry.io -> AI (blackmatrix-openai)`
- decision: `prefer-category` -> `HOST-SUFFIX,sentry.io -> AI (blackmatrix-openai)` (The configured business-category priority applies to this conflict.)

## ai ↔ proxy

### 474. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)`
- right: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)` (Blackmatrix is the configured primary source.)

### 475. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 476. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 477. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 478. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 479. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 480. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 481. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this conflict.)

### 482. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 483. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 484. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 485. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 486. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 487. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 488. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 489. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,openai -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 490. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 491. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 492. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 493. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 494. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 495. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 496. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 497. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 498. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 499. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 500. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (A more specific rule takes precedence over a broader overlap.)

### 501. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 502. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 503. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 504. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 505. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 506. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 507. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 508. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (A more specific rule takes precedence over a broader overlap.)

### 509. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 510. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 511. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

### 512. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (A more specific rule takes precedence over a broader overlap.)

## apple ↔ google

### 513. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this conflict.)

## apple ↔ microsoft

### 514. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)` (The configured business-category priority applies to this conflict.)

### 515. semantic-overlap / host-inside-host-suffix
- left: `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 516. semantic-overlap / host-inside-host-suffix
- left: `HOST,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 517. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 518. semantic-overlap / host-inside-host-suffix
- left: `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 519. semantic-overlap / host-inside-host-suffix
- left: `HOST,cds.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,cds.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 520. semantic-overlap / host-inside-host-suffix
- left: `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 521. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 522. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 523. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 524. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 525. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 526. semantic-overlap / host-inside-host-suffix
- left: `HOST,configuration.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,configuration.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 527. semantic-overlap / host-inside-host-suffix
- left: `HOST,courier-push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,courier-push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 528. semantic-overlap / host-inside-host-suffix
- left: `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 529. semantic-overlap / host-inside-host-suffix
- left: `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 530. semantic-overlap / host-inside-host-suffix
- left: `HOST,e16991.b.akamaiedge.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,b.akamaiedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,e16991.b.akamaiedge.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 531. semantic-overlap / host-inside-host-suffix
- left: `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 532. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 533. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 534. semantic-overlap / host-inside-host-suffix
- left: `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 535. semantic-overlap / host-inside-host-suffix
- left: `HOST,images.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,images.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 536. semantic-overlap / host-inside-host-suffix
- left: `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 537. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 538. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 539. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 540. semantic-overlap / host-inside-host-suffix
- left: `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 541. semantic-overlap / host-inside-host-suffix
- left: `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 542. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 543. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 544. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 545. semantic-overlap / host-inside-host-suffix
- left: `HOST,ocsp-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,ocsp-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 546. semantic-overlap / host-inside-host-suffix
- left: `HOST,ocsp2-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,ocsp2-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 547. semantic-overlap / host-inside-host-suffix
- left: `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 548. semantic-overlap / host-inside-host-suffix
- left: `HOST,pancake.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,pancake.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 549. semantic-overlap / host-inside-host-suffix
- left: `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 550. semantic-overlap / host-inside-host-suffix
- left: `HOST,push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 551. semantic-overlap / host-inside-host-suffix
- left: `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 552. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 553. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 554. semantic-overlap / host-inside-host-suffix
- left: `HOST,support-china.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,support-china.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 555. semantic-overlap / host-inside-host-suffix
- left: `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 556. semantic-overlap / host-inside-host-suffix
- left: `HOST,swdist.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,swdist.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 557. semantic-overlap / host-inside-host-suffix
- left: `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 558. semantic-overlap / host-inside-host-suffix
- left: `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 559. semantic-overlap / host-inside-host-suffix
- left: `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 560. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 561. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 562. semantic-overlap / host-inside-host-suffix
- left: `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 563. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 564. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

## apple ↔ global-media

### 565. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 566. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 567. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 568. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 569. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 570. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 571. semantic-overlap / host-inside-host-suffix
- left: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 572. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 573. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

## apple ↔ proxy

### 574. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 575. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 576. exact-policy / same-rule-different-policy
- left: `HOST,beta.music.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,beta.music.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 577. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 578. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 579. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 580. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 581. exact-policy / same-rule-different-policy
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 582. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 583. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 584. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 585. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 586. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 587. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 588. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 589. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 590. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `prefer-specific` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 591. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 592. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 593. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 594. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 595. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 596. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)`
- decision: `prefer-specific` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 597. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 598. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 599. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 600. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 601. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (A more specific rule takes precedence over a broader overlap.)

### 602. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 603. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 604. semantic-overlap / host-inside-host-suffix
- left: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 605. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 606. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 607. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 608. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 609. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 610. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 611. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 612. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 613. semantic-overlap / host-inside-host-suffix
- left: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 614. semantic-overlap / host-inside-host-suffix
- left: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 615. semantic-overlap / host-inside-host-suffix
- left: `HOST,facetime.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,facetime.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 616. semantic-overlap / host-inside-host-suffix
- left: `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 617. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,books.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 618. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `prefer-specific` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 619. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 620. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 621. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,testflight -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 622. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 623. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

## google-voice ↔ google

### 624. exact-policy / same-rule-different-policy
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this conflict.)

### 625. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this conflict.)

### 626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this conflict.)

## google-voice ↔ proxy

### 627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `prefer-specific` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (A more specific rule takes precedence over a broader overlap.)

## google ↔ social

### 628. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

### 629. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

### 630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- decision: `prefer-category` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (The configured business-category priority applies to this conflict.)

## google ↔ youtube

### 631. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 632. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 633. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 634. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 635. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 636. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 637. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 638. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 639. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 640. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 641. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 642. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 643. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 644. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 645. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 646. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 647. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 648. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 649. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 650. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 651. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 652. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 653. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 654. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 655. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 656. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 657. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

## google ↔ global-media

### 658. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 659. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 660. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

## google ↔ proxy

### 661. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 662. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 663. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 664. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 665. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 666. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 667. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 668. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 669. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 670. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 671. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 672. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 673. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 674. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 675. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,appspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 676. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,blogspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)` (A more specific rule takes precedence over a broader overlap.)

### 677. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 678. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 679. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,fonts.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,fonts.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 680. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 681. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 682. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing-cache.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,safebrowsing-cache.google.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 683. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 684. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,translate.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,translate.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 686. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 691. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 692. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 693. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 694. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 695. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 696. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 697. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 698. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 699. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 700. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 701. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 702. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 703. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 704. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 705. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 706. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 707. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 708. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 709. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 710. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 711. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 712. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 713. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 714. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 715. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 716. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 717. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 718. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 719. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 720. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 721. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 722. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 723. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 729. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 730. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 731. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 732. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 733. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 734. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 735. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 736. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 737. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 738. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 739. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 740. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 741. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 742. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 743. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 744. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 745. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 746. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 747. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 748. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 749. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 750. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 751. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 752. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 753. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 754. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 755. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 756. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 757. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 758. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 765. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 766. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 767. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 768. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 769. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 770. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 771. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 772. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 773. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 774. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 775. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 776. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 777. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 778. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 779. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 780. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 781. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 782. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 783. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 784. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 785. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 786. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 787. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 788. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 789. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 790. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 791. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 792. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 793. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 794. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 795. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 796. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 797. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 798. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 799. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 800. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 801. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 802. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 803. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 804. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 805. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 806. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 807. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 808. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 809. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 810. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 811. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 812. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 813. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 814. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 815. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 816. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 817. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 818. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 819. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 820. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 821. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 822. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 823. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 824. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 825. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 826. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 827. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 828. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 829. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 830. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 831. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 832. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 833. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 834. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 835. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 836. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 837. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 838. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 839. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 840. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 841. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 842. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 843. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 844. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 845. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 846. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 847. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 848. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 849. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 850. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 851. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 852. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 853. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 854. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 855. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 856. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 857. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 858. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 859. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 860. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 861. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 862. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 863. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 864. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 865. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 866. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 867. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 868. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 869. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 870. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 871. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 872. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 873. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 874. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 875. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 876. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 877. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 878. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 879. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 880. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 881. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 882. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 883. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 884. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 885. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 886. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 887. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 888. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 889. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 890. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 891. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 892. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 893. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 894. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 895. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 896. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 897. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 898. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 899. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 900. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 901. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 902. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 903. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 904. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 905. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 906. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 907. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 908. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 909. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 910. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 911. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 912. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 913. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 914. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 915. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 916. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 917. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 918. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 919. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 920. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 921. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 922. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 924. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 925. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 926. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 927. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 928. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 929. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 930. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 931. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 932. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 933. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 934. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 935. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 936. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 937. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 938. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 939. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 940. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 941. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 942. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 943. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 944. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 945. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 946. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 947. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)` (A more specific rule takes precedence over a broader overlap.)

### 948. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `prefer-specific` -> `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)` (A more specific rule takes precedence over a broader overlap.)

### 949. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `prefer-specific` -> `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)` (A more specific rule takes precedence over a broader overlap.)

### 950. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 951. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 952. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 953. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 954. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 955. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 956. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 957. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 958. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 959. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 960. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 961. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 962. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 963. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 964. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

### 965. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `prefer-specific` -> `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ spotify

### 966. semantic-overlap / host-inside-host-suffix
- left: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ netflix

### 967. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 968. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

## microsoft ↔ global-media

### 969. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)` (A more specific rule takes precedence over a broader overlap.)

### 970. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 971. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-specific` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 972. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)`
- decision: `prefer-specific` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)` (A more specific rule takes precedence over a broader overlap.)

## social ↔ netflix

### 973. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.226.106.180/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.226.106.180/32 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 974. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.226.14.0/24 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.226.14.0/24 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 975. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.228.4.208/28 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.228.4.208/28 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 976. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.114.205/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.231.114.205/32 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 977. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.213.21/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.231.213.21/32 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 978. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.236.241.44/30 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.236.241.44/30 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 979. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.238.188.0/29 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,34.238.188.0/29 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

### 980. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,54.243.31.192/26 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,54.242.0.0/15 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `prefer-category` -> `IP-CIDR,54.243.31.192/26 -> Netflix (blackmatrix-netflix)` (The configured business-category priority applies to this conflict.)

## developer ↔ github

### 981. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npm.community -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 982. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

### 983. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.org -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this conflict.)

## developer ↔ global-media

### 984. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (blackmatrix-global-media-abema-tv)`
- decision: `prefer-specific` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)` (A more specific rule takes precedence over a broader overlap.)

## github ↔ proxy

### 985. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 986. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 987. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 988. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 989. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 990. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 991. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 992. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 993. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 994. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 995. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 996. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

### 997. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,github.global.ssl.fastly.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this conflict.)

## spotify ↔ global-media

### 998. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 999. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 1000. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 1001. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 1002. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 1003. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 1004. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 1005. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1006. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1007. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1008. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1009. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1010. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1011. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

### 1012. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `prefer-specific` -> `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (A more specific rule takes precedence over a broader overlap.)

## telegram ↔ proxy

### 1013. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1014. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1015. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1016. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1017. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1018. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1019. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1020. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1021. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1022. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1023. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1024. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1025. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1026. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1027. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1028. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1029. exact-policy / same-rule-different-policy
- left: `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1030. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23f::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1031. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:67c:4e8::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 1032. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1033. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1034. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1035. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1036. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1037. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1038. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1039. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

### 1040. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this conflict.)

## tiktok ↔ global-media

### 1041. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1042. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1043. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1044. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1045. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1046. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1047. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1048. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 1049. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1050. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1051. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1052. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1053. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1054. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1055. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-category` -> `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

### 1056. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this conflict.)

## youtube ↔ global-media

### 1057. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1058. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1059. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1060. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1061. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1062. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1063. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1064. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1065. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1066. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1067. exact-policy / same-rule-different-policy
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1068. exact-policy / same-rule-different-policy
- left: `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1069. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1070. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1071. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-category` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1072. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1073. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1074. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1075. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1076. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1077. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1078. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

### 1079. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,youtube.* -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-WILDCARD,youtube.* -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this conflict.)

## youtube ↔ proxy

### 1080. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 1081. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1082. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1083. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1084. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1085. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1086. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1087. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

### 1088. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A more specific rule takes precedence over a broader overlap.)

## netflix ↔ global-media

### 1089. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1090. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1091. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1092. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1093. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1094. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1095. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1096. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1097. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1098. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1099. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1100. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,onetrust.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)` (A more specific rule takes precedence over a broader overlap.)

### 1101. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1102. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1103. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 1104. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1105. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1106. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1107. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1108. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1109. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1110. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1111. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1112. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1113. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1114. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

### 1115. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-WILDCARD,netflixdnstest*.com -> Netflix (blackmatrix-netflix)`
- decision: `prefer-specific` -> `HOST-WILDCARD,netflixdnstest*.com -> Netflix (blackmatrix-netflix)` (A more specific rule takes precedence over a broader overlap.)

## china-media ↔ global-media

### 1116. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1117. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1118. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1119. exact-policy / same-rule-different-policy
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1120. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1121. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1122. exact-policy / same-rule-different-policy
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1123. exact-policy / same-rule-different-policy
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1124. exact-policy / same-rule-different-policy
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1125. exact-policy / same-rule-different-policy
- left: `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1126. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1127. exact-policy / same-rule-different-policy
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1128. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1129. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1130. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.206/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1131. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.216/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

### 1132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this conflict.)

## global-media ↔ proxy

### 1133. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source.)

### 1134. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this conflict.)

### 1135. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)` (Blackmatrix is the configured primary source.)

### 1136. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this conflict.)

### 1137. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 1138. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)

### 1139. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (A more specific rule takes precedence over a broader overlap.)
