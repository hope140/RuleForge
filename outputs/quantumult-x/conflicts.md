# RuleForge conflict report

These 280 entries were evaluated by the source-priority resolver.
Priority: Blackmatrix, direct over reject, and specific host rules over broader host rules.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 126
- semantic-overlap: 154
- resolved: 257
- blackmatrix-preferred: 176
- direct-preferred: 7
- specific-preferred: 74
- unresolved: 23

## reject ↔ china-direct

### 1. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-blackmatrix` -> `HOST,ad.12306.cn -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

### 2. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## reject ↔ direct-exception

### 3. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.appsflyer.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,appsflyer.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,app.appsflyer.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 4. semantic-overlap / host-inside-host-suffix
- left: `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,tagtic.cn -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 5. semantic-overlap / host-inside-host-suffix
- left: `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 6. semantic-overlap / host-inside-host-suffix
- left: `HOST,livew.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,livew.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 7. semantic-overlap / host-inside-host-suffix
- left: `HOST,vd.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vd.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

### 8. semantic-overlap / host-inside-host-suffix
- left: `HOST,vi.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `prefer-direct` -> `HOST,vi.l.qq.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## reject ↔ apple

### 9. semantic-overlap / host-inside-host-suffix
- left: `HOST,iadsdk.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST,iadsdk.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 10. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

## reject ↔ google

### 11. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 12. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 13. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 14. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 15. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## reject ↔ tiktok

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## reject ↔ youtube

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## reject ↔ global-media

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 20. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 21. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-specific` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

## reject ↔ proxy

### 22. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 23. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 24. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 25. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 26. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 27. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 28. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 29. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 30. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 31. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 32. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 33. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 34. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 35. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 36. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 37. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

### 38. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `prefer-specific` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (A specific host rule takes precedence over a broader host rule.)

## privacy ↔ china-direct

### 39. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `prefer-blackmatrix` -> `HOST,tracking.miui.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## privacy ↔ direct-exception

### 40. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.adjust.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,adjust.com -> reject (rulego-tracking)`
- decision: `prefer-direct` -> `HOST,app.adjust.com -> direct (rulego-direct-plus)` (direct takes precedence over reject.)

## privacy ↔ ai

### 41. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 42. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,segment.io -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,segment.io -> AI (blackmatrix-copilot)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,segment.io -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

## privacy ↔ apple

### 43. semantic-overlap / host-inside-host-suffix
- left: `HOST,token.safebrowsing.apple -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,safebrowsing.apple -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,safebrowsing.apple -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

## privacy ↔ google

### 44. exact-policy / same-rule-different-policy
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 45. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 46. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 47. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## privacy ↔ proxy

### 48. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (A specific host rule takes precedence over a broader host rule.)

### 49. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (A specific host rule takes precedence over a broader host rule.)

### 50. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,c.bing.com -> reject (rulego-tracking)` (A specific host rule takes precedence over a broader host rule.)

### 51. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (A specific host rule takes precedence over a broader host rule.)

## china-direct ↔ apple

### 52. exact-policy / same-rule-different-policy
- left: `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 53. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 54. exact-policy / same-rule-different-policy
- left: `HOST,smp-device-content.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 55. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 56. semantic-overlap / host-inside-host-suffix
- left: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,init.ess.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 57. semantic-overlap / host-inside-host-suffix
- left: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 58. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)` (A specific host rule takes precedence over a broader host rule.)

### 59. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)` (A specific host rule takes precedence over a broader host rule.)

### 60. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,itunes.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 61. semantic-overlap / host-inside-host-suffix
- left: `HOST,time.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-specific` -> `HOST,time.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 62. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-analytics-events.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST-SUFFIX,weather-analytics-events.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 63. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 64. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-specific` -> `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

## china-direct ↔ google

### 65. exact-policy / same-rule-different-policy
- left: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 66. exact-policy / same-rule-different-policy
- left: `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 67. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 68. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (blackmatrix-direct)`
- decision: `unresolved`

### 69. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,clientservices.googleapis.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 70. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 71. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 72. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 73. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 74. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 75. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 76. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 77. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

### 78. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (A specific host rule takes precedence over a broader host rule.)

## china-direct ↔ proxy

### 79. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ google

### 80. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 81. exact-policy / same-rule-different-policy
- left: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 82. exact-policy / same-rule-different-policy
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 83. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 84. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 85. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 86. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 87. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 88. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 89. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 90. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ youtube

### 91. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## direct-exception ↔ proxy

### 92. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (A specific host rule takes precedence over a broader host rule.)

## ai ↔ apple

### 93. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 94. exact-policy / same-rule-different-policy
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 95. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 96. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 97. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 98. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 99. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 100. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 101. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 102. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 103. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 104. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 105. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 106. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,mzstatic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 107. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

## ai ↔ google

### 108. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

### 109. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 110. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 111. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 112. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 113. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 114. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 115. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 116. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 117. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 118. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 119. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 120. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 121. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

### 122. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 123. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 124. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 125. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `prefer-specific` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (A specific host rule takes precedence over a broader host rule.)

## ai ↔ github

### 126. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 127. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 128. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

## ai ↔ proxy

### 129. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 130. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 131. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 132. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source.)

### 133. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 134. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 135. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 136. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 137. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 138. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 139. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 140. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 141. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `prefer-specific` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (A specific host rule takes precedence over a broader host rule.)

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 143. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (A specific host rule takes precedence over a broader host rule.)

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (A specific host rule takes precedence over a broader host rule.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `prefer-specific` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (A specific host rule takes precedence over a broader host rule.)

### 148. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source.)

## apple ↔ google

### 149. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

## apple ↔ global-media

### 150. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 151. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 152. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 153. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 154. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 155. semantic-overlap / host-inside-host-suffix
- left: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 156. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

## apple ↔ proxy

### 157. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 158. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 159. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 160. exact-policy / same-rule-different-policy
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 161. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 162. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 163. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 164. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 165. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 166. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 167. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 168. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 169. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 170. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 171. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 172. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 173. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source.)

## google-voice ↔ google

### 180. exact-policy / same-rule-different-policy
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (A specific host rule takes precedence over a broader host rule.)

## google ↔ youtube

### 182. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

### 183. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

### 184. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `unresolved`

### 185. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 186. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 187. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 188. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 189. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 190. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 191. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 192. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 193. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 194. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 195. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 196. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-specific` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (A specific host rule takes precedence over a broader host rule.)

### 197. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 198. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 199. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

### 200. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-specific` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (A specific host rule takes precedence over a broader host rule.)

## google ↔ global-media

### 201. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## google ↔ proxy

### 202. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 203. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 204. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 205. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 206. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 207. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 208. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 209. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 210. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 211. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 212. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 213. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 214. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

### 215. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source.)

## github ↔ proxy

### 216. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 217. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 218. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 219. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 220. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 221. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

### 222. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source.)

## spotify ↔ global-media

### 223. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 224. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 225. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

### 226. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source.)

## telegram ↔ proxy

### 227. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 228. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 229. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 230. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 231. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 232. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 233. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 234. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 235. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 236. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 237. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 238. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 239. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 240. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 241. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

### 242. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (Blackmatrix is the configured primary source.)

## tiktok ↔ global-media

### 243. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 244. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 245. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 246. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 247. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 248. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 249. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

### 250. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source.)

## youtube ↔ global-media

### 251. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 252. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 253. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 254. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 255. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 256. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 257. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 258. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 259. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 260. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 261. exact-policy / same-rule-different-policy
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 262. exact-policy / same-rule-different-policy
- left: `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 263. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 264. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

### 265. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## youtube ↔ proxy

### 266. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source.)

## netflix ↔ global-media

### 267. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 268. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 269. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 270. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 271. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 272. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 273. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 274. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 275. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 276. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

### 277. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source.)

## global-media ↔ proxy

### 278. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 279. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `unresolved`

### 280. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-specific` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (A specific host rule takes precedence over a broader host rule.)
