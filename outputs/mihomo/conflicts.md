# RuleForge conflict report

These 928 entries were evaluated by the source-priority resolver.
Exact conflicts use business and security priorities; semantic overlaps retain both rules and record first-match ordering.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 174
- semantic-overlap: 754
- resolved: 928
- blackmatrix-preferred: 58
- direct-preferred: 0
- specific-preferred: 0
- category-preferred: 105
- protective-reject: 11
- ordered-overlap: 754
- unresolved: 0

## direct-exception ↔ reject

### 1. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.appsflyer.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,appsflyer.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,app.appsflyer.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 2. semantic-overlap / host-inside-host-suffix
- left: `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,tagtic.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,bdtj.tagtic.cn -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 3. semantic-overlap / host-inside-host-suffix
- left: `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,fairplay.l.qq.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 4. semantic-overlap / host-inside-host-suffix
- left: `HOST,livew.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,livew.l.qq.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 5. semantic-overlap / host-inside-host-suffix
- left: `HOST,vd.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,vd.l.qq.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 6. semantic-overlap / host-inside-host-suffix
- left: `HOST,vi.l.qq.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,vi.l.qq.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 7. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

### 8. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

## direct-exception ↔ privacy

### 9. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.adjust.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,adjust.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,app.adjust.com -> direct (rulego-direct-plus)` (Both rules are retained. An explicit direct-exception may override reject.)

## direct-exception ↔ youtube

### 10. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## direct-exception ↔ google

### 11. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 12. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 13. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 14. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,ci.android.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 15. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 20. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 21. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 22. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 23. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 24. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 25. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 26. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## direct-exception ↔ proxy

### 27. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 28. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 29. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 30. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 31. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 32. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 33. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 34. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## reject ↔ youtube

### 35. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 36. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ tiktok

### 37. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST,pangolin.snssdk.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ social

### 38. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 39. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 40. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 41. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,twitter -> 全球加速 (blackmatrix-social-twitter)`
- right: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ google

### 42. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,admob.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 43. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 44. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 45. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 46. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 47. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 48. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 49. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 50. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 51. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 52. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 53. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 54. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ microsoft

### 55. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 56. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,msads.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 57. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 58. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 59. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 60. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 61. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 62. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 63. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ global-media

### 64. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 65. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 66. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)`
- decision: `ordered-overlap` -> `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 67. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 68. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 69. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 70. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 71. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 72. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 73. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 74. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 75. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-services

### 76. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-reject` -> `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 77. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)`
- decision: `ordered-overlap` -> `HOST,ad.12306.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 78. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 79. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,afd.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 80. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,als.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 81. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,duclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 82. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 83. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 84. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 85. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 86. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nsclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 87. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 88. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 89. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 90. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 91. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,sax.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 92. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxn.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 93. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxs.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 94. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 95. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 96. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 97. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 98. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 99. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 100. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 101. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 102. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 103. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-streaming

### 104. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ad.mobile.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 105. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,iyes.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 106. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ykad-data.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 107. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 108. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 109. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 110. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 111. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 112. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 113. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 114. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-direct

### 115. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-reject` -> `HOST,ad.12306.cn -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 116. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,adsp.xunlei.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 117. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 118. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ proxy

### 119. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 120. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 121. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 122. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 123. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 124. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 125. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 126. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 127. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 128. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 129. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 130. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 131. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 133. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,.pinterest -> 全球加速 (rulego-proxy)`
- right: `HOST,ads.pinterest.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.pinterest.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ social

### 134. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 135. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ google

### 136. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 137. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 138. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 139. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 140. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 141. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ microsoft

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,c.bing.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ global-media

### 143. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-services

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hm.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hmma.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 148. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 149. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,flash.sec.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 150. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,tracking.intl.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 151. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 152. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 153. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-direct

### 154. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ proxy

### 155. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 156. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 157. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 158. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## ai ↔ tiktok

### 159. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source tie-breaker.)

## ai ↔ developer

### 160. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source tie-breaker.)

### 161. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source tie-breaker.)

### 162. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ github

### 163. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source tie-breaker.)

### 164. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 165. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 166. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 167. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 168. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ apple

### 169. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source tie-breaker.)

### 170. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ social

### 171. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source tie-breaker.)

### 172. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)`
- decision: `ordered-overlap` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ google

### 173. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this exact conflict.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 180. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 183. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 184. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 185. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 186. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 187. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 188. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 189. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 190. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 191. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 192. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 193. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 194. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 195. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 196. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 197. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 198. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 199. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 200. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 201. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 202. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 203. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 204. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 205. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 206. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 207. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 208. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 209. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 210. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 211. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 212. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 213. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## ai ↔ microsoft

### 214. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 215. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 216. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 217. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 218. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 219. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 220. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 221. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 222. semantic-overlap / host-inside-host-suffix
- left: `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,appcenter.ms -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 223. semantic-overlap / host-inside-host-suffix
- left: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 224. semantic-overlap / host-inside-host-suffix
- left: `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,live.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 225. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 226. semantic-overlap / host-inside-host-suffix
- left: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 227. semantic-overlap / host-inside-host-suffix
- left: `HOST,services.bingapis.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bingapis.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,services.bingapis.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 228. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 229. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 230. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 231. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 232. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 233. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 234. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 235. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 236. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 237. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 238. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 239. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 240. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 241. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 242. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 243. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 244. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 245. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 246. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ global-media

### 247. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

## ai ↔ china-direct

### 248. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 249. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ proxy

### 250. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)`
- right: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)` (Blackmatrix is the configured primary source tie-breaker.)

### 251. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 252. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 253. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source tie-breaker.)

### 254. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source tie-breaker.)

### 255. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 256. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 257. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 258. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 259. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 260. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 261. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source tie-breaker.)

### 262. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 263. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 264. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 265. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,openai -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 266. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 267. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 268. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 269. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 270. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 271. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 272. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 273. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 274. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 275. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 276. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 277. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 278. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 279. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 280. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 281. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 282. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 283. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 284. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 285. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 286. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 287. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 288. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google-voice ↔ google

### 289. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 290. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google-voice ↔ proxy

### 291. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## youtube ↔ google

### 292. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 293. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 294. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 295. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 296. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 297. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 298. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 299. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 300. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 301. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 302. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 303. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 304. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 305. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 306. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 307. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 308. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 309. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 310. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 311. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 312. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 313. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 314. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 315. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## youtube ↔ global-media

### 316. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 317. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 318. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 319. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 320. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 321. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 322. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 323. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 324. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 325. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 326. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 327. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 328. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube-music)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 329. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 330. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 331. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 332. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 333. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 334. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 335. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## youtube ↔ proxy

### 336. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source tie-breaker.)

### 337. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 338. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 339. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 340. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 341. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 342. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 343. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ microsoft

### 344. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 345. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ global-media

### 346. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 347. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 348. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 349. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 350. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 351. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 352. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 353. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 354. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 355. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 356. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 357. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,onetrust.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 358. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 359. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 360. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 361. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 362. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 363. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 364. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 365. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 366. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 367. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 368. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 369. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 370. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 371. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## tiktok ↔ global-media

### 372. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 373. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 374. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 375. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 376. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 377. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 378. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 379. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 380. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 381. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 382. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 383. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 384. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 385. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 386. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 387. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## telegram ↔ proxy

### 388. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 389. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 390. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 391. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 392. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 393. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 394. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 395. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 396. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 397. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 398. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 399. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 400. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 401. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 402. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 403. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 404. exact-policy / same-rule-different-policy
- left: `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 405. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23f::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 406. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:67c:4e8::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 407. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 408. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 409. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 410. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 411. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 412. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 413. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 414. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 415. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## spotify ↔ microsoft

### 416. semantic-overlap / host-inside-host-suffix
- left: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## spotify ↔ global-media

### 417. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 418. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 419. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 420. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 421. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 422. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 423. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 424. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 425. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 426. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 427. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 428. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 429. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 430. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 431. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## developer ↔ github

### 432. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npm.community -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

### 433. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

### 434. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.org -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

## developer ↔ global-media

### 435. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (blackmatrix-global-media-abema-tv)`
- decision: `ordered-overlap` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ proxy

### 436. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 437. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 438. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 439. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 440. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 441. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 442. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 443. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 444. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 445. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 446. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 447. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 448. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,github.global.ssl.fastly.net -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## apple ↔ global-media

### 449. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 450. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 451. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 452. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 453. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 454. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ china-direct

### 455. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (The configured business-category priority applies to this exact conflict.)

### 456. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this exact conflict.)

### 457. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 458. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 459. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 460. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gsa.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)`
- decision: `ordered-overlap` -> `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 461. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 462. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `ordered-overlap` -> `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 463. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `ordered-overlap` -> `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 464. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `ordered-overlap` -> `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple-proxy)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 465. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- decision: `ordered-overlap` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## apple ↔ proxy

### 466. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 467. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 468. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 469. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 470. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-appstore)` (Blackmatrix is the configured primary source tie-breaker.)

### 471. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 472. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple-media)` (Blackmatrix is the configured primary source tie-breaker.)

### 473. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 474. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 475. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple-news)` (Blackmatrix is the configured primary source tie-breaker.)

### 476. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 477. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 478. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-proxy)` (Blackmatrix is the configured primary source tie-breaker.)

### 479. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 480. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 481. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 482. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 483. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 484. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 485. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `ordered-overlap` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 486. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)`
- decision: `ordered-overlap` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 487. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 488. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,testflight -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## social ↔ google

### 489. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 490. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 491. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google ↔ global-media

### 492. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 493. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 494. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ china-services

### 495. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 496. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ china-direct

### 497. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 498. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 499. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 500. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 501. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 502. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 503. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 504. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 505. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 506. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 507. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 508. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 509. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 510. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 511. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 512. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 513. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 514. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google ↔ proxy

### 515. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 516. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 517. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 518. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 519. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 520. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 521. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 522. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 523. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 524. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 525. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 526. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 527. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 528. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,appspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 529. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,blogspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 530. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 531. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 532. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 533. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 534. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 535. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 536. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 537. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 538. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 539. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 540. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 541. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 542. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 543. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 544. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 545. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 546. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 547. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 548. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 549. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 550. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 551. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 552. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 553. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 554. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 555. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 556. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 557. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 558. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 559. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 560. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 561. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 562. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 563. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 564. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 565. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 566. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 567. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 568. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 569. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 570. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 571. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 572. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 573. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 574. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 575. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 576. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 577. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 578. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 579. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 580. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 581. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 582. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 583. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 584. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 585. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 586. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 587. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 588. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 589. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 590. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 591. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 592. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 593. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 594. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 595. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 596. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 597. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 598. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 599. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 600. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 601. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 602. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 603. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 604. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 605. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 606. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 607. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 608. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 609. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 610. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 611. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 612. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 613. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 614. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 615. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 616. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 617. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 618. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 619. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 620. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 621. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 622. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 623. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 624. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 625. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 628. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 629. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 631. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 632. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 633. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 634. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 635. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 636. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 637. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 638. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 639. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 640. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 641. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 642. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 643. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 644. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 645. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 646. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 647. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 648. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 649. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 650. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 651. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 652. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 653. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 654. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 655. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 656. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 657. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 658. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 659. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 660. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 661. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 662. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 663. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 664. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 665. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 666. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 667. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 668. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 669. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 670. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 671. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 672. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 673. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 674. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 675. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 676. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 677. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 678. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 679. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 680. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 681. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 682. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 683. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 684. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 686. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 691. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 692. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 693. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 694. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 695. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 696. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 697. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 698. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 699. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 700. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 701. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 702. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 703. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 704. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 705. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 706. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 707. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 708. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 709. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 710. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 711. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 712. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 713. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 714. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 715. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 716. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 717. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 718. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 719. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 720. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 721. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 722. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 723. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 729. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 730. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 731. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 732. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 733. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 734. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 735. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 736. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 737. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 738. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 739. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 740. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 741. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 742. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 743. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 744. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 745. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 746. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 747. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 748. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 749. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 750. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 751. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 752. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 753. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 754. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 755. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 756. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 757. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 758. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 765. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 766. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 767. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 768. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 769. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 770. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 771. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 772. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 773. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 774. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 775. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 776. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 777. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 778. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 779. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 780. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 781. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 782. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 783. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 784. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 785. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 786. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 787. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 788. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 789. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 790. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 791. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 792. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `ordered-overlap` -> `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google-drive)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 793. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 794. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 795. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 796. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 797. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 798. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 799. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 800. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 801. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 802. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 803. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 804. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 805. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 806. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 807. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 808. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 809. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 810. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## microsoft ↔ global-media

### 811. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 812. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 813. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 814. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-media ↔ global-media

### 815. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 816. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 817. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 818. exact-policy / same-rule-different-policy
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 819. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 820. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 821. exact-policy / same-rule-different-policy
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 822. exact-policy / same-rule-different-policy
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 823. exact-policy / same-rule-different-policy
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 824. exact-policy / same-rule-different-policy
- left: `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 825. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 826. exact-policy / same-rule-different-policy
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 827. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 828. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 829. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.206/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 830. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.216/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 831. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## china-media ↔ china-streaming

### 832. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 833. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 834. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 835. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 836. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 837. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 838. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 839. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 840. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 841. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 842. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 843. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## global-media ↔ china-streaming

### 844. exact-policy / same-rule-different-policy
- left: `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 845. exact-policy / same-rule-different-policy
- left: `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 846. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 847. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 848. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)`
- right: `HOST-SUFFIX,bilibili.tv -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)` (The configured business-category priority applies to this exact conflict.)

### 849. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 850. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 851. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 852. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 853. exact-policy / same-rule-different-policy
- left: `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 854. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 855. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 856. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 857. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 858. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 859. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 860. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 861. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 862. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 863. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 864. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 865. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 866. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 867. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 868. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this exact conflict.)

### 869. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 870. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 871. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 872. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 873. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 874. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 875. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 876. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 877. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 878. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 879. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 880. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 881. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 882. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 883. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 884. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 885. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 886. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 887. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 888. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 889. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 890. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 891. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 892. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 893. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 894. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 895. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 896. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 897. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 898. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 899. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 900. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 901. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 902. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 903. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 904. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 905. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## global-media ↔ china-direct

### 906. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## global-media ↔ proxy

### 907. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source tie-breaker.)

### 908. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 909. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)` (Blackmatrix is the configured primary source tie-breaker.)

### 910. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 911. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 912. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 913. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-services ↔ proxy

### 914. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 915. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-direct ↔ proxy

### 916. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source tie-breaker.)

### 917. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source tie-breaker.)

### 918. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,amp-api.podcasts.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 919. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 920. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 921. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 922. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 924. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 925. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 926. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 927. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 928. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)
