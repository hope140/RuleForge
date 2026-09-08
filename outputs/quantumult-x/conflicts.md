# RuleForge conflict report

These 1137 entries were evaluated by the source-priority resolver.
Exact conflicts use business and security priorities; semantic overlaps retain both rules and record first-match ordering.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 193
- semantic-overlap: 944
- resolved: 1137
- blackmatrix-preferred: 66
- direct-preferred: 0
- specific-preferred: 0
- category-preferred: 113
- protective-reject: 14
- ordered-overlap: 944
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
- left: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 13. exact-policy / same-rule-different-policy
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 14. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 15. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 16. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,ci.android.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 20. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 21. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 22. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 23. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 24. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 25. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 26. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 27. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 28. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## direct-exception ↔ proxy

### 29. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 30. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 31. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 32. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 33. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 34. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 35. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 36. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## reject ↔ youtube

### 37. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 38. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ tiktok

### 39. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST,pangolin.snssdk.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ apple

### 40. semantic-overlap / host-inside-host-suffix
- left: `HOST,iadsdk.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 41. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ social

### 42. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 43. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 44. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 45. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,twitter -> 全球加速 (blackmatrix-social-twitter)`
- right: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ google

### 46. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,admob.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 47. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 48. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 49. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 50. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 51. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 52. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 53. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 54. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 55. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 56. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 57. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 58. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ microsoft

### 59. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 60. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,msads.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 61. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 62. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 63. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 64. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 65. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 66. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 67. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ global-media

### 68. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 69. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 70. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (blackmatrix-global-media-amazon-prime-video)`
- decision: `ordered-overlap` -> `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 71. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 72. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 73. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 74. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 75. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 76. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 77. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 78. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 79. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-services

### 80. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tanx.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tanx.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-reject` -> `HOST-SUFFIX,tanx.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 81. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yukhj.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yukhj.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `prefer-reject` -> `HOST-SUFFIX,yukhj.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 82. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (blackmatrix-china-services-baidu)`
- decision: `prefer-reject` -> `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 83. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (blackmatrix-china-services-12306)`
- decision: `ordered-overlap` -> `HOST,ad.12306.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 84. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 85. semantic-overlap / host-inside-host-suffix
- left: `HOST,hc-ssp.sm.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sm.cn -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,hc-ssp.sm.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 86. semantic-overlap / host-inside-host-suffix
- left: `HOST,tunion-api.m.taobao.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,taobao.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,tunion-api.m.taobao.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 87. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,amap.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,optimus-ads.amap.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 88. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com.w.alikunlun.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,alikunlun.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,optimus-ads.amap.com.w.alikunlun.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 89. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,afd.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 90. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,als.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 91. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,duclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 92. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 93. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 94. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 95. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 96. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nsclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 97. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstore-index-1252524079.file.myqcloud.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,myqcloud.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adstore-index-1252524079.file.myqcloud.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 98. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 99. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 100. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 101. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 102. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,sax.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 103. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxn.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 104. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxs.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 105. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 106. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 107. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.gdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.gdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 108. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.tc.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 109. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.ugdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 110. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.cn -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 111. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 112. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.ugdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 113. semantic-overlap / host-inside-host-suffix
- left: `HOST,splashqqlive.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,splashqqlive.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 114. semantic-overlap / host-inside-host-suffix
- left: `HOST,wa.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,wa.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 115. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ad.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 116. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 117. semantic-overlap / host-inside-host-suffix
- left: `HOST,tmead.y.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,tmead.y.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 118. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adchina.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,afp.adchina.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adchina.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 119. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 120. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 121. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 122. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 123. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 124. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 125. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 126. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 127. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 128. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 129. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 130. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (blackmatrix-china-services-sina)`
- right: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-streaming

### 131. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ad.mobile.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 132. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,iyes.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 133. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ykad-data.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 134. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 135. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 136. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 137. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (blackmatrix-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 138. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 139. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 140. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 141. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-direct

### 142. exact-policy / same-rule-different-policy
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST,ad.12306.cn -> direct (blackmatrix-direct)`
- decision: `prefer-reject` -> `HOST,ad.12306.cn -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 143. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,adsp.xunlei.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 144. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-KEYWORD,api-adservices.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 145. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ma-adx.ctrip.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ proxy

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 148. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 149. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 150. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 151. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 152. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 153. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 154. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 155. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 156. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 157. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 158. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 159. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 160. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,.pinterest -> 全球加速 (rulego-proxy)`
- right: `HOST,ads.pinterest.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.pinterest.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ apple

### 161. semantic-overlap / host-inside-host-suffix
- left: `HOST,token.safebrowsing.apple -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,safebrowsing.apple -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,token.safebrowsing.apple -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ social

### 162. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 163. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (blackmatrix-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ google

### 164. exact-policy / same-rule-different-policy
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 165. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 166. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 167. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 168. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 169. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 170. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ microsoft

### 171. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,c.bing.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ global-media

### 172. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-services

### 173. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hm.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (blackmatrix-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hmma.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,flash.sec.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,tracking.intl.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 180. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.urlsec.qq.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,qq.com -> direct (blackmatrix-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.urlsec.qq.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 183. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (blackmatrix-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-direct

### 184. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ proxy

### 185. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 186. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 187. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 188. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## ai ↔ tiktok

### 189. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (Blackmatrix is the configured primary source tie-breaker.)

## ai ↔ developer

### 190. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source tie-breaker.)

### 191. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (blackmatrix-developer-jetbrains)` (Blackmatrix is the configured primary source tie-breaker.)

### 192. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (blackmatrix-developer-jetbrains)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ github

### 193. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)` (Blackmatrix is the configured primary source tie-breaker.)

### 194. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 195. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 196. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubcopilot.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 197. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 198. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ apple

### 199. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 200. exact-policy / same-rule-different-policy
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `prefer-blackmatrix` -> `HOST,guzzoni.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 201. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 202. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 203. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 204. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 205. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 206. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 207. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,apps.mzstatic.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 208. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 209. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 210. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 211. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 212. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,mzstatic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 213. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ social

### 214. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,grok.com -> 全球加速 (blackmatrix-social-twitter)` (Blackmatrix is the configured primary source tie-breaker.)

### 215. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (blackmatrix-social-facebook)`
- decision: `ordered-overlap` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ google

### 216. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (blackmatrix-gemini)` (The configured business-category priority applies to this exact conflict.)

### 217. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 218. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 219. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 220. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 221. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 222. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 223. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 224. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 225. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 226. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 227. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 228. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 229. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 230. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 231. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 232. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 233. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 234. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 235. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 236. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 237. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 238. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 239. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 240. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 241. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 242. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 243. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 244. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 245. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 246. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 247. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 248. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 249. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 250. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 251. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 252. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 253. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 254. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 255. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 256. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## ai ↔ microsoft

### 257. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 258. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 259. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,production-openaicom-storage.azureedge.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 260. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,api.msn.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 261. semantic-overlap / host-inside-host-suffix
- left: `HOST,assets.msn.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,assets.msn.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 262. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 263. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 264. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 265. semantic-overlap / host-inside-host-suffix
- left: `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,appcenter.ms -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,in.appcenter.ms -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 266. semantic-overlap / host-inside-host-suffix
- left: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 267. semantic-overlap / host-inside-host-suffix
- left: `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,live.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,odc.officeapps.live.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 268. semantic-overlap / host-inside-host-suffix
- left: `HOST,r.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,r.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 269. semantic-overlap / host-inside-host-suffix
- left: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 270. semantic-overlap / host-inside-host-suffix
- left: `HOST,services.bingapis.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bingapis.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,services.bingapis.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 271. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,sydney.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 272. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bing.com -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,www.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 273. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaiapi-site.azureedge.net -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 274. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 275. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 276. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (blackmatrix-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 277. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 278. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 279. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 280. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 281. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 282. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 283. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 284. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,location.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,location.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 285. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST,self.events.data.microsoft.com -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 286. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 287. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (blackmatrix-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 288. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 289. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ global-media

### 290. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

## ai ↔ china-direct

### 291. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 292. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ proxy

### 293. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)`
- right: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,civitai.com -> AI (blackmatrix-civitai)` (Blackmatrix is the configured primary source tie-breaker.)

### 294. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 295. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 296. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,chatgpt.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source tie-breaker.)

### 297. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,openai.com -> AI (blackmatrix-openai)` (Blackmatrix is the configured primary source tie-breaker.)

### 298. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 299. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 300. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

### 301. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 302. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 303. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 304. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,copilot.microsoft.com -> AI (blackmatrix-copilot)` (Blackmatrix is the configured primary source tie-breaker.)

### 305. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 306. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 307. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gateway.icloud.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 308. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,openai -> AI (blackmatrix-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 309. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 310. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 311. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 312. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 313. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,makersuite.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 314. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 315. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 316. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 317. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 318. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 319. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (blackmatrix-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 320. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 321. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 322. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 323. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 324. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 325. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 326. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 327. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 328. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 329. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 330. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 331. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google-voice ↔ google

### 332. exact-policy / same-rule-different-policy
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (The configured business-category priority applies to this exact conflict.)

### 333. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 334. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google-voice ↔ proxy

### 335. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (blackmatrix-google-voice)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## youtube ↔ google

### 336. exact-policy / same-rule-different-policy
- left: `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,172.110.32.0/21 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,172.110.32.0/21 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 337. exact-policy / same-rule-different-policy
- left: `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)`
- right: `IP-CIDR,216.73.80.0/20 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP-CIDR,216.73.80.0/20 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 338. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)`
- right: `IP6-CIDR,2620:120:e000::/40 -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `IP6-CIDR,2620:120:e000::/40 -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 339. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 340. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 341. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 342. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 343. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 344. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt2.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 345. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 346. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 347. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 348. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 349. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 350. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 351. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 352. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 353. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 354. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 355. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 356. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 357. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 358. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 359. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 360. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 361. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 362. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## youtube ↔ global-media

### 363. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 364. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,withyoutube.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 365. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtu.be -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 366. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 367. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 368. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 369. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtubekids.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 370. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 371. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,yt.be -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 372. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ytimg.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 373. exact-policy / same-rule-different-policy
- left: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 374. exact-policy / same-rule-different-policy
- left: `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)`
- right: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST,yt3.ggpht.com -> YouTube (blackmatrix-youtube)` (The configured business-category priority applies to this exact conflict.)

### 375. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,music.youtube.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 376. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 377. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggpht.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 378. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 379. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 380. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 381. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 382. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 383. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 384. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 385. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,youtube.* -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,youtube.* -> YouTube (blackmatrix-youtube)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## youtube ↔ proxy

### 386. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt1.com -> YouTube (blackmatrix-youtube)` (Blackmatrix is the configured primary source tie-breaker.)

### 387. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 388. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 389. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 390. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 391. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 392. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 393. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 394. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (blackmatrix-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ social

### 395. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.226.106.180/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.226.106.180/32 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 396. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.226.14.0/24 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.226.14.0/24 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 397. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.228.4.208/28 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.228.4.208/28 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 398. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.114.205/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.231.114.205/32 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 399. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.213.21/32 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.231.213.21/32 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 400. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.236.241.44/30 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.236.241.44/30 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 401. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.238.188.0/29 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.238.188.0/29 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 402. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,54.243.31.192/26 -> Netflix (blackmatrix-netflix)`
- right: `IP-CIDR,54.242.0.0/15 -> 全球加速 (blackmatrix-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,54.243.31.192/26 -> Netflix (blackmatrix-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## netflix ↔ microsoft

### 403. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 404. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ global-media

### 405. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,fast.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 406. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 407. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,netflix.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 408. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxext.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 409. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.com -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 410. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflximg.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 411. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxso.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 412. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 413. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 414. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 415. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Blackmatrix is the configured primary source tie-breaker.)

### 416. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,onetrust.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,disney-portal.my.onetrust.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 417. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 418. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 419. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,netflixdnstest -> Netflix (blackmatrix-netflix)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 420. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest0.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 421. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest1.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 422. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest10.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 423. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest2.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 424. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest3.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 425. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest4.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 426. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest5.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 427. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest6.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 428. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest7.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 429. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest8.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 430. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest9.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 431. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-WILDCARD,netflixdnstest*.com -> Netflix (blackmatrix-netflix)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,netflixdnstest*.com -> Netflix (blackmatrix-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## tiktok ↔ global-media

### 432. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 433. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 434. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 435. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 436. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 437. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 438. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 439. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (blackmatrix-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 440. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,musical.ly -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 441. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 442. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 443. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 444. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 445. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 446. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 447. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (blackmatrix-tiktok)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## telegram ↔ proxy

### 448. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 449. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,comments.app -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 450. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,graph.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 451. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,legra.ph -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 452. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 453. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,t.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 454. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 455. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 456. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 457. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 458. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 459. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.space -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 460. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 461. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 462. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tg.dev -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 463. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tx.me -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 464. exact-policy / same-rule-different-policy
- left: `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,149.154.160.0/20 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 465. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23f::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 466. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:67c:4e8::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (blackmatrix-telegram)` (The configured business-category priority applies to this exact conflict.)

### 467. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 468. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 469. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 470. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 471. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 472. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.0.0/16 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 473. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 474. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 475. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2a0a:f280::/29 -> 电报代理 (blackmatrix-telegram)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## spotify ↔ microsoft

### 476. semantic-overlap / host-inside-host-suffix
- left: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## spotify ↔ global-media

### 477. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,pscdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 478. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,scdn.co -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 479. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 480. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,spoti.fi -> Spotify (blackmatrix-spotify)` (Blackmatrix is the configured primary source tie-breaker.)

### 481. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 482. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 483. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (blackmatrix-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 484. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,spotify.com.edgesuite.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 485. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,byspotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 486. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 487. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tospotify.com -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 488. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 489. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 490. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 491. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (blackmatrix-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## developer ↔ github

### 492. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npm.community -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npm.community -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

### 493. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.com -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

### 494. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,npmjs.org -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)`
- decision: `prefer-category` -> `HOST-SUFFIX,npmjs.org -> 全球加速 (blackmatrix-developer-npmjs)` (The configured business-category priority applies to this exact conflict.)

## developer ↔ global-media

### 495. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (blackmatrix-global-media-abema-tv)`
- decision: `ordered-overlap` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (blackmatrix-developer-docker)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## developer ↔ china-services

### 496. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (blackmatrix-developer-gitlab)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (blackmatrix-developer-gitlab)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ china-services

### 497. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (blackmatrix-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ proxy

### 498. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,git.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,git.io -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 499. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.blog -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 500. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 501. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.io -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 502. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubassets.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 503. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (blackmatrix-github)` (The configured business-category priority applies to this exact conflict.)

### 504. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 505. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 506. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 507. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 508. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 509. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 510. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (blackmatrix-github)`
- right: `HOST,github.global.ssl.fastly.net -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (blackmatrix-github)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## apple ↔ google

### 511. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this exact conflict.)

## apple ↔ microsoft

### 512. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 513. semantic-overlap / host-inside-host-suffix
- left: `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 514. semantic-overlap / host-inside-host-suffix
- left: `HOST,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 515. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 516. semantic-overlap / host-inside-host-suffix
- left: `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 517. semantic-overlap / host-inside-host-suffix
- left: `HOST,cds.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,cds.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 518. semantic-overlap / host-inside-host-suffix
- left: `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 519. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 520. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 521. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 522. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 523. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 524. semantic-overlap / host-inside-host-suffix
- left: `HOST,configuration.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,configuration.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 525. semantic-overlap / host-inside-host-suffix
- left: `HOST,courier-push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,courier-push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 526. semantic-overlap / host-inside-host-suffix
- left: `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 527. semantic-overlap / host-inside-host-suffix
- left: `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 528. semantic-overlap / host-inside-host-suffix
- left: `HOST,e16991.b.akamaiedge.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,b.akamaiedge.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,e16991.b.akamaiedge.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 529. semantic-overlap / host-inside-host-suffix
- left: `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 530. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 531. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 532. semantic-overlap / host-inside-host-suffix
- left: `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 533. semantic-overlap / host-inside-host-suffix
- left: `HOST,images.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,images.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 534. semantic-overlap / host-inside-host-suffix
- left: `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 535. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 536. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 537. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 538. semantic-overlap / host-inside-host-suffix
- left: `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 539. semantic-overlap / host-inside-host-suffix
- left: `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 540. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,itunes-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 541. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 542. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 543. semantic-overlap / host-inside-host-suffix
- left: `HOST,ocsp-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,ocsp-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 544. semantic-overlap / host-inside-host-suffix
- left: `HOST,ocsp2-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,ocsp2-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 545. semantic-overlap / host-inside-host-suffix
- left: `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 546. semantic-overlap / host-inside-host-suffix
- left: `HOST,pancake.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,pancake.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 547. semantic-overlap / host-inside-host-suffix
- left: `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 548. semantic-overlap / host-inside-host-suffix
- left: `HOST,push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,push-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 549. semantic-overlap / host-inside-host-suffix
- left: `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 550. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 551. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 552. semantic-overlap / host-inside-host-suffix
- left: `HOST,support-china.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,support-china.apple-support.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 553. semantic-overlap / host-inside-host-suffix
- left: `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 554. semantic-overlap / host-inside-host-suffix
- left: `HOST,swdist.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,swdist.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 555. semantic-overlap / host-inside-host-suffix
- left: `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 556. semantic-overlap / host-inside-host-suffix
- left: `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 557. semantic-overlap / host-inside-host-suffix
- left: `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 558. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 559. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 560. semantic-overlap / host-inside-host-suffix
- left: `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 561. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 562. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ global-media

### 563. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,tv.applemusic.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 564. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 565. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-blackmatrix` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 566. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 567. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 568. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 569. semantic-overlap / host-inside-host-suffix
- left: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 570. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 571. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ china-services

### 572. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,autonavi.com -> direct (blackmatrix-china-services-alibaba)`
- right: `HOST-SUFFIX,dispatcher.is.autonavi.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dispatcher.is.autonavi.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ china-direct

### 573. exact-policy / same-rule-different-policy
- left: `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this exact conflict.)

### 574. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this exact conflict.)

### 575. exact-policy / same-rule-different-policy
- left: `HOST,smp-device-content.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,smp-device-content.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this exact conflict.)

### 576. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (The configured business-category priority applies to this exact conflict.)

### 577. semantic-overlap / host-inside-host-suffix
- left: `HOST,init.ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 578. semantic-overlap / host-inside-host-suffix
- left: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 579. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,weather-data.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 580. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,weather-map.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 581. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 582. semantic-overlap / host-inside-host-suffix
- left: `HOST,time.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 583. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-analytics-events.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 584. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-data.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 585. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,weather-map.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 586. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,buy.itunes.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,buy.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 587. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,smp-device-content.apple.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,smp-device -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 588. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 589. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,api.smoot.apple.cn -> direct (blackmatrix-direct)`
- right: `HOST,api.smoot.apple.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,api.smoot.apple.cn -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 590. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,init.ess.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 591. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ess.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.fitness.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,amp-api.fitness.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 592. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gsa.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)`
- decision: `ordered-overlap` -> `HOST,gsa.apple.com -> 苹果服务 (blackmatrix-apple-id)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 593. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 594. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,icloud-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 595. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,mask-api.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 596. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,mask-h2.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 597. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,mask.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 598. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,fmfmobile.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,fmfmobile.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 599. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,fmipmobile.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,fmipmobile.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 600. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,statici.icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,statici.icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 601. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 602. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,applemx-icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,applemx-icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 603. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 604. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,icloud.com.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,icloud.com.cn -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 605. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,ios-icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ios-icloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 606. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,wwwicloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wwwicloud.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 607. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-WILDCARD,*-content.icloud.com.cn -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,*-content.icloud.com.cn -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 608. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mail.icloud.com.cn -> 苹果服务 (blackmatrix-apple-mail)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 609. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp10-ssl-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp10-ssl-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 610. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp12-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp12-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 611. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp13-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp13-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 612. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp4-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 613. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 614. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 615. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp5-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp5-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 616. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gsp85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gsp85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 617. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe11-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe11-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 618. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe12-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe12-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 619. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe19-2-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 620. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe19-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 621. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe19-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe19-cn.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 622. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe21-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe21-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 623. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe21.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe21.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 624. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe35-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe35-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 625. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe79-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe79-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe85-cn-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 628. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 629. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,ls.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init-p01st.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,init-p01st.push.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 631. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,init-s01st.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,init-s01st.push.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 632. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,push.apple.com -> direct (blackmatrix-direct)`
- right: `HOST-WILDCARD,init*.push.apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,init*.push.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## apple ↔ proxy

### 633. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,testflight.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 634. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 635. exact-policy / same-rule-different-policy
- left: `HOST,beta.music.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,beta.music.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 636. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,books.itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 637. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,lookup-api.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 638. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apps.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 639. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 640. exact-policy / same-rule-different-policy
- left: `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,gateway.icloud.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 641. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apple.news -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 642. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-assets.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 643. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 644. exact-policy / same-rule-different-policy
- left: `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-client-search.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 645. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-edge.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 646. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,news-events.apple.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 647. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)` (Blackmatrix is the configured primary source tie-breaker.)

### 648. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 649. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (blackmatrix-apple-proxy)`
- decision: `ordered-overlap` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 650. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,apps.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 651. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-c.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 652. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-d.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 653. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-p-ap-e.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 654. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (blackmatrix-apple-music)`
- decision: `ordered-overlap` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 655. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 656. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,icloud.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 657. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 658. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 659. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (blackmatrix-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 660. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 661. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 662. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 663. semantic-overlap / host-inside-host-suffix
- left: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 664. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 665. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 666. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 667. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 668. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 669. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 670. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 671. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 672. semantic-overlap / host-inside-host-suffix
- left: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 673. semantic-overlap / host-inside-host-suffix
- left: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 674. semantic-overlap / host-inside-host-suffix
- left: `HOST,facetime.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,facetime.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 675. semantic-overlap / host-inside-host-suffix
- left: `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 676. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,books.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 677. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (blackmatrix-apple-media)`
- decision: `ordered-overlap` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 678. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- decision: `ordered-overlap` -> `HOST,tv.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 679. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 680. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,testflight -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 681. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (blackmatrix-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 682. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (blackmatrix-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## social ↔ google

### 683. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 684. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (blackmatrix-social-discord)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google ↔ global-media

### 686. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ china-services

### 689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.cn -> direct (blackmatrix-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.com -> direct (blackmatrix-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ china-direct

### 691. exact-policy / same-rule-different-policy
- left: `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `prefer-category` -> `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)` (The configured business-category priority applies to this exact conflict.)

### 692. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 693. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 694. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 695. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 696. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 697. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 698. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 699. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 700. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 701. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 702. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 703. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 704. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 705. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 706. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 707. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 708. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 709. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## google ↔ proxy

### 710. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 711. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 712. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 713. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 714. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 715. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 716. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 717. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 718. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (blackmatrix-google)` (Blackmatrix is the configured primary source tie-breaker.)

### 719. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 720. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 721. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 722. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 723. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,appspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,blogspot -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. Blackmatrix is the configured primary source tie-breaker.)

### 727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,fonts.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,fonts.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 729. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 730. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 731. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing-cache.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing-cache.google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 732. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 733. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,translate.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,translate.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 734. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,www.googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 735. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 736. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 737. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 738. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 739. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 740. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 741. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 742. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 743. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 744. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ad -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 745. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ae -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 746. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.al -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 747. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.am -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 748. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.as -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 749. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.at -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 750. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.az -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 751. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ba -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 752. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.be -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 753. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.berlin -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 754. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bf -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 755. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 756. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 757. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 758. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bs -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.by -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ca -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cat -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cd -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cf -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 765. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 766. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ch -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 767. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ci -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 768. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 769. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 770. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 771. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ao -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 772. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.bw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 773. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ck -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 774. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.cr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 775. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.id -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 776. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.il -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 777. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.in -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 778. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.jp -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 779. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ke -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 780. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.kr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 781. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ls -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 782. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ma -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 783. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.mz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 784. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.nz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 785. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.th -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 786. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.tz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 787. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ug -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 788. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 789. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 790. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ve -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 791. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.vi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 792. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.za -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 793. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 794. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 795. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 796. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.af -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 797. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ag -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 798. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ai -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 799. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ar -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 800. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.au -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 801. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bd -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 802. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 803. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 804. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bo -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 805. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.br -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 806. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 807. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.co -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 808. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 809. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 810. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.do -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 811. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ec -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 812. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.eg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 813. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.et -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 814. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.fj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 815. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 816. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 817. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 818. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.hk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 819. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.jm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 820. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 821. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 822. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.lb -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 823. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ly -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 824. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 825. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 826. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mx -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 827. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.my -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 828. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.na -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 829. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ng -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 830. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ni -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 831. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.np -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 832. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.om -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 833. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 834. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pe -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 835. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 836. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ph -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 837. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 838. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 839. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.py -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 840. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.qa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 841. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sa -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 842. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sb -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 843. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 844. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 845. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 846. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 847. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 848. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 849. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ua -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 850. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.uy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 851. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vc -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 852. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 853. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 854. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 855. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.de -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 856. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dev -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 857. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dj -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 858. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 859. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 860. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 861. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ee -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 862. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.es -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 863. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fi -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 864. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 865. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 866. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ga -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 867. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ge -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 868. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 869. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 870. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 871. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 872. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gy -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 873. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 874. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 875. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ht -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 876. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 877. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ie -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 878. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.im -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 879. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.iq -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 880. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.is -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 881. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.it -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 882. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.je -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 883. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.jo -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 884. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 885. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ki -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 886. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kz -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 887. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.la -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 888. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.li -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 889. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 890. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 891. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 892. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 893. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.md -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 894. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.me -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 895. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 896. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 897. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ml -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 898. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 899. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ms -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 900. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 901. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mv -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 902. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 903. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ne -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 904. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 905. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 906. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.no -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 907. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 908. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 909. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.org -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 910. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 911. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 912. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ps -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 913. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 914. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ro -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 915. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rs -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 916. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ru -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 917. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rw -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 918. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sc -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 919. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.se -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 920. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sh -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 921. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.si -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 922. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 924. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 925. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.so -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 926. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sr -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 927. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.st -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 928. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.td -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 929. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 930. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tl -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 931. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tm -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 932. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 933. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.to -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 934. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tt -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 935. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ventures -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 936. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vg -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 937. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vu -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 938. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ws -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 939. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 940. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 941. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 942. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 943. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 944. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 945. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 946. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 947. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 948. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 949. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlearth.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 950. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleblog.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 951. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlebot.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 952. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 953. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecert.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 954. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 955. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecode.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 956. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 957. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 958. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 959. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledomains.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 960. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlee.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 961. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleearth.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 962. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 963. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 964. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 965. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 966. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemail.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 967. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 968. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 969. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 970. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 971. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 972. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 973. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplay.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 974. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplus.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 975. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 976. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesource.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 977. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlestore.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 978. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 979. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 980. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 981. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 982. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 983. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 984. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 985. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 986. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 987. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 988. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleventures.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 989. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,igoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 990. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 991. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,registry.google -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 992. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 993. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 994. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 995. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledrive.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 996. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (blackmatrix-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 997. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,docs.google.com -> 谷歌服务 (blackmatrix-google-drive)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 998. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,drive.google.com -> 谷歌服务 (blackmatrix-google-drive)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 999. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1000. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1001. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,kh.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1002. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1003. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1004. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1005. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1006. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1007. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1008. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1009. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1010. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1011. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1012. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1013. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1014. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (blackmatrix-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## microsoft ↔ global-media

### 1015. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (blackmatrix-global-media-tvb)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1016. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1017. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (blackmatrix-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1018. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (blackmatrix-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (blackmatrix-global-media-hbo)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-media ↔ global-media

### 1019. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1020. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1021. exact-policy / same-rule-different-policy
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1022. exact-policy / same-rule-different-policy
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1023. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1024. exact-policy / same-rule-different-policy
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1025. exact-policy / same-rule-different-policy
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1026. exact-policy / same-rule-different-policy
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1027. exact-policy / same-rule-different-policy
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1028. exact-policy / same-rule-different-policy
- left: `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,mobileso.bz.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,mobileso.bz.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1029. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1030. exact-policy / same-rule-different-policy
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1031. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1032. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1033. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.206/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.206/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1034. exact-policy / same-rule-different-policy
- left: `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)`
- right: `IP-CIDR,116.211.202.216/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `prefer-category` -> `IP-CIDR,116.211.202.216/32 -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1035. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)`
- right: `HOST-KEYWORD,cn-hk-eq-bcache- -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,cn-hk-eq-bcache- -> 港台番剧 (rulego-china-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## china-media ↔ china-streaming

### 1036. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1037. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1038. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1039. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1040. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1041. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1042. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1043. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1044. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1045. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1046. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1047. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## global-media ↔ china-services

### 1048. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,joox.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,joox.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,joox.com -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source tie-breaker.)

### 1049. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,wetv.vip -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,wetv.vip -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,wetv.vip -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source tie-breaker.)

### 1050. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,wetvinfo.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,wetvinfo.com -> direct (blackmatrix-china-services-tencent)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,wetvinfo.com -> direct (blackmatrix-china-services-tencent)` (Blackmatrix is the configured primary source tie-breaker.)

## global-media ↔ china-streaming

### 1051. exact-policy / same-rule-different-policy
- left: `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,p-bstarstatic.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,p-bstarstatic.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1052. exact-policy / same-rule-different-policy
- left: `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,p.bstarstatic.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,p.bstarstatic.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1053. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-bstar-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1054. exact-policy / same-rule-different-policy
- left: `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)`
- right: `HOST,upos-bstar1-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-bstar1-mirrorakam.akamaized.net -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1055. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)`
- right: `HOST-SUFFIX,bilibili.tv -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (blackmatrix-global-media-bilibili-intl)` (The configured business-category priority applies to this exact conflict.)

### 1056. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1057. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1058. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1059. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,103.5.34.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1060. exact-policy / same-rule-different-policy
- left: `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,104.109.129.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1061. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1062. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1063. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1064. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.169/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1065. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.193/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1066. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1067. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1068. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.153/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1069. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.11/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1070. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.8/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1071. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.200/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1072. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1073. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1074. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (blackmatrix-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1075. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (The configured business-category priority applies to this exact conflict.)

### 1076. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.53.32.88/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1077. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1078. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1079. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1080. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1081. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1082. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1083. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,grpc.biliapi.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1084. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,m.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1085. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1086. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,bilibili.com -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,www.bilibili.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1087. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1088. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (blackmatrix-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1089. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1090. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1091. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1092. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1093. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1094. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1095. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1096. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1097. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1098. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1099. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1100. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1101. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1102. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1103. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1104. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1105. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1106. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1107. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1108. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1109. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (blackmatrix-china-streaming-iqiyi)`
- right: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (blackmatrix-global-media-asian)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1110. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1111. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.162/32 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1112. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (blackmatrix-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,23.211.15.0/24 -> 国际媒体 (blackmatrix-global-media-iqiyi-intl)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## global-media ↔ china-direct

### 1113. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,trip.com -> direct (blackmatrix-direct)`
- right: `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,disneychannelroadtrip.com -> 国际媒体 (blackmatrix-global-media-disney)` (Both rules are retained. The configured business-category priority provides the first-match order.)

## global-media ↔ proxy

### 1114. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,abc.com -> 国际媒体 (blackmatrix-global-media-disney)` (Blackmatrix is the configured primary source tie-breaker.)

### 1115. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1116. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST-SUFFIX,now.com -> 国际媒体 (blackmatrix-global-media-hbo)` (Blackmatrix is the configured primary source tie-breaker.)

### 1117. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (The configured business-category priority applies to this exact conflict.)

### 1118. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1119. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1120. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-services ↔ proxy

### 1121. semantic-overlap / host-inside-host-suffix
- left: `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1122. semantic-overlap / host-inside-host-suffix
- left: `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (blackmatrix-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1123. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1124. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (blackmatrix-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-direct ↔ proxy

### 1125. exact-policy / same-rule-different-policy
- left: `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)`
- right: `HOST,cdn.jsdelivr.net -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,cdn.jsdelivr.net -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source tie-breaker.)

### 1126. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-blackmatrix` -> `HOST,itunes.apple.com -> direct (blackmatrix-direct)` (Blackmatrix is the configured primary source tie-breaker.)

### 1127. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,amp-api.podcasts.apple.com -> direct (blackmatrix-direct)`
- right: `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,amp-api.podcasts.apple.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1128. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,icloud.com -> direct (blackmatrix-direct)`
- right: `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,gateway.icloud.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1129. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt1-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1130. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt2-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1131. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt3-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt4-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1133. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt5-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1134. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt6-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1135. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt7-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1136. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,alt8-mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1137. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> direct (blackmatrix-direct)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> direct (blackmatrix-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)
