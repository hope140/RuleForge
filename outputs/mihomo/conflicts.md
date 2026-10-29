# RuleForge conflict report

These 2035 entries were evaluated by the business-priority resolver.
Exact conflicts use security, explicit override, specificity, category semantics and same-category source priority; semantic overlaps retain both rules and record first-match ordering.
Conflicts that match none of these priorities remain unresolved and are excluded.

## Summary

- exact-policy: 316
- semantic-overlap: 1719
- resolved: 2035
- blackmatrix-preferred: 0
- source-preferred: 0
- direct-preferred: 0
- specific-preferred: 0
- category-preferred: 228
- value-category-preferred: 64
- protective-reject: 24
- fallback: 0
- ordered-overlap: 1719
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

## direct-exception ↔ google

### 10. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blog.google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 11. exact-policy / same-rule-different-policy
- left: `HOST,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 12. exact-policy / same-rule-different-policy
- left: `HOST,dl.google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 13. exact-policy / same-rule-different-policy
- left: `HOST,dl.l.google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 14. exact-policy / same-rule-different-policy
- left: `HOST,update.googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 15. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 16. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `prefer-category` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (The configured business-category priority applies to this exact conflict.)

### 17. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 18. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 19. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,dl.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 20. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 21. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,dl.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 22. semantic-overlap / host-inside-host-suffix
- left: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 23. semantic-overlap / host-inside-host-suffix
- left: `HOST,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 24. semantic-overlap / host-inside-host-suffix
- left: `HOST,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,googletraveladservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 25. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,update.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 26. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 27. semantic-overlap / host-inside-host-suffix
- left: `HOST,ci.android.com -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,android.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,ci.android.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 28. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 29. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 30. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 31. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 32. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 33. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 34. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 35. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## direct-exception ↔ proxy

### 36. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 37. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 38. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 39. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 40. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 41. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 42. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> direct (rulego-direct-plus)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## reject ↔ youtube

### 43. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads.youtube.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 44. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 45. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ tiktok

### 46. semantic-overlap / host-inside-host-suffix
- left: `HOST,pangolin.snssdk.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,snssdk.com -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST,pangolin.snssdk.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ apple

### 47. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-reject` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 48. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iadsdk.apple.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 49. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,api-adservices.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ social

### 50. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads-twitter.com -> 全球加速 (magicrule-social-twitter)`
- decision: `prefer-reject` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 51. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 全球加速 (magicrule-social-line)`
- decision: `ordered-overlap` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 52. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (magicrule-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 53. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (magicrule-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.g.daum.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 54. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,twitter -> 全球加速 (magicrule-social-twitter)`
- right: `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads-twitter.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ google

### 55. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,admob.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,admob.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 56. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,doubleclick.net -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 57. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 58. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadsserving.cn -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 59. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 60. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 61. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.admob.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,admob.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 62. semantic-overlap / host-inside-host-suffix
- left: `HOST,doubleclick.net -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,doubleclick.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 63. semantic-overlap / host-inside-host-suffix
- left: `HOST,googleadservices.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 64. semantic-overlap / host-inside-host-suffix
- left: `HOST,googlesyndication.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 65. semantic-overlap / host-inside-host-suffix
- left: `HOST,googletagservices.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 66. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,admob.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,c.admob.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,admob.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 67. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST,adservice.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 68. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST,googleadservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 69. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST,googleadservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 70. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 71. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 72. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adservice.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 73. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 74. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 75. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 76. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 77. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 78. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 79. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 80. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ microsoft

### 81. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,localytics.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,localytics.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 82. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,msads.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msads.net -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-reject` -> `HOST-SUFFIX,msads.net -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 83. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobileads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,mobileads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 84. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 85. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads1.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 86. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,msn.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads2.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 87. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 88. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,msn.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,rads.msn.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 89. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bingads.microsoft.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ global-media

### 90. semantic-overlap / host-inside-host-suffix
- left: `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ameba.jp -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,abema-adx.ameba.jp -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 91. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserver.pandora.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pandora.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,adserver.pandora.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 92. semantic-overlap / host-inside-host-suffix
- left: `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,llnwd.net -> 国际媒体 (magicrule-global-media-amazon-prime-video)`
- decision: `ordered-overlap` -> `HOST,appnext.hs.llnwd.net -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 93. semantic-overlap / host-inside-host-suffix
- left: `HOST,itad.linetv.tw -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,itad.linetv.tw -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 94. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.youtube.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,ads.youtube.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 95. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-01.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 96. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-02.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 97. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-03.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 98. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-04.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 99. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-05.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 100. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-06.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 101. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,braze.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iad-08.braze.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-services

### 102. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tanx.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tanx.com -> direct (magicrule-china-services-alibaba)`
- decision: `prefer-reject` -> `HOST-SUFFIX,tanx.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 103. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yukhj.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yukhj.com -> direct (magicrule-china-services-alibaba)`
- decision: `prefer-reject` -> `HOST-SUFFIX,yukhj.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 104. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,cpro.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `prefer-reject` -> `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 105. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,duapps.com -> direct (magicrule-china-services-baidu)`
- decision: `prefer-reject` -> `HOST-SUFFIX,duapps.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 106. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pos.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `prefer-reject` -> `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 107. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,e.qq.com -> direct (magicrule-china-services-tencent)`
- decision: `prefer-reject` -> `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 108. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gdt.qq.com -> direct (magicrule-china-services-tencent)`
- decision: `prefer-reject` -> `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 109. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tjqonline.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tjqonline.cn -> direct (magicrule-china-services-xiaomi)`
- decision: `prefer-reject` -> `HOST-SUFFIX,tjqonline.cn -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 110. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,alitui.weibo.com -> direct (magicrule-china-services-sina)`
- decision: `prefer-reject` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 111. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,beacon.sina.com.cn -> direct (magicrule-china-services-sina)`
- decision: `prefer-reject` -> `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 112. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.12306.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,12306.cn -> direct (magicrule-china-services-12306)`
- decision: `ordered-overlap` -> `HOST,ad.12306.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 113. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ad.xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 114. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.ad.xiaomi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 115. semantic-overlap / host-inside-host-suffix
- left: `HOST,business-cdn.shouji.sogou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sogou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,business-cdn.shouji.sogou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 116. semantic-overlap / host-inside-host-suffix
- left: `HOST,hc-ssp.sm.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sm.cn -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,hc-ssp.sm.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 117. semantic-overlap / host-inside-host-suffix
- left: `HOST,tunion-api.m.taobao.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,taobao.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,tunion-api.m.taobao.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 118. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,optimus-ads.amap.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,optimus-ads.amap.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 119. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,amap.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,optimus-ads.amap.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 120. semantic-overlap / host-inside-host-suffix
- left: `HOST,optimus-ads.amap.com.w.alikunlun.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,alikunlun.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,optimus-ads.amap.com.w.alikunlun.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 121. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,afd.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,afd.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 122. semantic-overlap / host-inside-host-suffix
- left: `HOST,afd.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,afd.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 123. semantic-overlap / host-inside-host-suffix
- left: `HOST,als.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,als.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 124. semantic-overlap / host-inside-host-suffix
- left: `HOST,duclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,duclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 125. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,mobads.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 126. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 127. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,mobads-logs.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 128. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-logs.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 129. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,mobads-pre-config.cdn.bcebos.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 130. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,bcebos.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,mobads-pre-config.cdn.bcebos.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 131. semantic-overlap / host-inside-host-suffix
- left: `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nadvideo2.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 132. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,nsclick.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nsclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 133. semantic-overlap / host-inside-host-suffix
- left: `HOST,nsclick.baidu.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,nsclick.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 134. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstore-index-1252524079.file.myqcloud.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,myqcloud.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adstore-index-1252524079.file.myqcloud.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 135. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adimg.uve.weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 136. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 137. semantic-overlap / host-inside-host-suffix
- left: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 138. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,biz.weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 139. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 140. semantic-overlap / host-inside-host-suffix
- left: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 141. semantic-overlap / host-inside-host-suffix
- left: `HOST,sax.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,sax.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 142. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxn.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxn.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 143. semantic-overlap / host-inside-host-suffix
- left: `HOST,saxs.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,saxs.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 144. semantic-overlap / host-inside-host-suffix
- left: `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST,u1.img.mobile.sina.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 145. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adsmind.apdcdn.tc.qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 146. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.apdcdn.tc.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 147. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.gdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gdtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.gdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 148. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.tc.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.tc.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 149. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsmind.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsmind.ugdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 150. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,pgdt.gtimg.cn -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 151. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.cn -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.gtimg.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 152. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 153. semantic-overlap / host-inside-host-suffix
- left: `HOST,pgdt.ugdtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ugdtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,pgdt.ugdtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 154. semantic-overlap / host-inside-host-suffix
- left: `HOST,splashqqlive.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,splashqqlive.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 155. semantic-overlap / host-inside-host-suffix
- left: `HOST,wa.gtimg.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gtimg.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,wa.gtimg.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 156. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ad.tencentmusic.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ad.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 157. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ad.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 158. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adstats.tencentmusic.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 159. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tencentmusic.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adstats.tencentmusic.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 160. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserviceretry.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adserviceretry.kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adserviceretry.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 161. semantic-overlap / host-inside-host-suffix
- left: `HOST,adserviceretry.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adserviceretry.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 162. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.service.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ads.service.kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ads.service.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 163. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.service.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ads.service.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 164. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsfile.bssdlbig.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsfile.bssdlbig.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 165. semantic-overlap / host-inside-host-suffix
- left: `HOST,g.koowo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,koowo.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,g.koowo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 166. semantic-overlap / host-inside-host-suffix
- left: `HOST,kgmobilestat.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,kgmobilestat.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 167. semantic-overlap / host-inside-host-suffix
- left: `HOST,kgmobilestatbak.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,kgmobilestatbak.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 168. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobilelog.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,mobilelog.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 169. semantic-overlap / host-inside-host-suffix
- left: `HOST,mobilead.kuwo.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kuwo.cn -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,mobilead.kuwo.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 170. semantic-overlap / host-inside-host-suffix
- left: `HOST,rich.kuwo.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kuwo.cn -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,rich.kuwo.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 171. semantic-overlap / host-inside-host-suffix
- left: `HOST,tmead.y.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,tmead.y.qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,tmead.y.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 172. semantic-overlap / host-inside-host-suffix
- left: `HOST,tmead.y.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,y.qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,tmead.y.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 173. semantic-overlap / host-inside-host-suffix
- left: `HOST,tmead.y.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,tmead.y.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 174. semantic-overlap / host-inside-host-suffix
- left: `HOST,splashimgbssdl.yun.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,splashimgbssdl.yun.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 175. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsfilebssdlbig.tx.kugou.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsfilebssdlbig.tx.kugou.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 176. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,ad.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 177. semantic-overlap / host-inside-host-suffix
- left: `HOST,adbs.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adbs.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 178. semantic-overlap / host-inside-host-suffix
- left: `HOST,adse.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adse.ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adse.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 179. semantic-overlap / host-inside-host-suffix
- left: `HOST,adse.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adse.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 180. semantic-overlap / host-inside-host-suffix
- left: `HOST,adse.wsa.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adse.wsa.ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adse.wsa.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 181. semantic-overlap / host-inside-host-suffix
- left: `HOST,adse.wsa.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adse.wsa.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 182. semantic-overlap / host-inside-host-suffix
- left: `HOST,adbehavior.wsa.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adbehavior.wsa.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 183. semantic-overlap / host-inside-host-suffix
- left: `HOST,adbehavior.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adbehavior.ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adbehavior.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 184. semantic-overlap / host-inside-host-suffix
- left: `HOST,adbehavior.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adbehavior.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 185. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsebs.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adsebs.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 186. semantic-overlap / host-inside-host-suffix
- left: `HOST,adwbs.ximalaya.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ximalaya.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,adwbs.ximalaya.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 187. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,weibo.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 188. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- right: `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cpro.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 189. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- right: `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pos.baidu.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 190. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,sina.com.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacon.sina.com.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 191. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,e.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 192. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gdt.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 193. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,l.qq.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 194. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adserviceretry.kglink.cn -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 195. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,adservice -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,adserviceretry.kugou.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,adservice -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 196. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (magicrule-china-services-sina)`
- right: `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,alitui.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 197. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (magicrule-china-services-sina)`
- right: `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 198. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (magicrule-china-services-sina)`
- right: `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adimg.vue.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 199. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (magicrule-china-services-sina)`
- right: `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,adstrategy.biz.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 200. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,weibo -> direct (magicrule-china-services-sina)`
- right: `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,bootpreload.uve.weibo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-streaming

### 201. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,atm.youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `prefer-reject` -> `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 202. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ad.mobile.youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ad.mobile.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 203. semantic-overlap / host-inside-host-suffix
- left: `HOST,ad.mobile.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ad.mobile.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 204. semantic-overlap / host-inside-host-suffix
- left: `HOST,iyes.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,iyes.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 205. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,ykad-data.youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ykad-data.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 206. semantic-overlap / host-inside-host-suffix
- left: `HOST,ykad-data.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST,ykad-data.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 207. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,cupid.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 208. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 209. semantic-overlap / host-inside-host-suffix
- left: `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,gitv.tv -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.ptqy.gitv.tv -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 210. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yk-ssp.ad.youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 211. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ad.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 212. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,youku.com -> direct (magicrule-china-streaming-youku)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,atm.youku.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 213. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,t7z.cupid.iqiyi.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 214. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 215. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.227.0.0/16 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.97.240/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 216. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 217. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.227.0.0/16 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.11/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 218. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.224.0.0/13 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 219. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)`
- right: `IP-CIDR,101.227.0.0/16 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,101.227.200.28/32 -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ china-direct

### 220. semantic-overlap / host-inside-host-suffix
- left: `HOST,adsp.xunlei.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,xunlei.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,adsp.xunlei.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## reject ↔ proxy

### 221. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 222. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads-d.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads-d.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 223. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.aws.viber.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,viber.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.aws.viber.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 224. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.auctions.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 225. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.finance.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 226. semantic-overlap / host-inside-host-suffix
- left: `HOST,ads.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,ads.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 227. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adserver.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 228. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adspecs.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 229. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,advertising.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 230. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)`
- right: `HOST-SUFFIX,yahoo.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.yahoo.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 231. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 232. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 233. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 234. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 235. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,.pinterest -> 全球加速 (rulego-proxy)`
- right: `HOST,ads.pinterest.com -> reject (rulego-advertising)`
- decision: `ordered-overlap` -> `HOST,ads.pinterest.com -> reject (rulego-advertising)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ apple

### 236. semantic-overlap / host-inside-host-suffix
- left: `HOST,token.safebrowsing.apple -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,safebrowsing.apple -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST,token.safebrowsing.apple -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 237. semantic-overlap / host-inside-host-suffix
- left: `HOST,token.safebrowsing.apple -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,apple -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST,token.safebrowsing.apple -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ social

### 238. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.daum.net -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,daum.net -> 全球加速 (magicrule-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.daum.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 239. semantic-overlap / host-inside-host-suffix
- left: `HOST,track.tiara.kakao.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,kakao.com -> 全球加速 (magicrule-social-kakaotalk)`
- decision: `ordered-overlap` -> `HOST,track.tiara.kakao.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ google

### 240. exact-policy / same-rule-different-policy
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 241. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-reject` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 242. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 243. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 244. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 245. semantic-overlap / host-inside-host-suffix
- left: `HOST,google-analytics.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 246. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 247. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 248. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ microsoft

### 249. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.bing.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,c.bing.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 250. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.clarity.ms -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,clarity.ms -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,c.clarity.ms -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 251. semantic-overlap / host-inside-host-suffix
- left: `HOST,o.clarity.ms -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,clarity.ms -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,o.clarity.ms -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 252. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.clarity.ms -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,clarity.ms -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,www.clarity.ms -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ global-media

### 253. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bam.nr-data.net -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,nr-data.net -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-services

### 254. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,tracking.miui.com -> direct (magicrule-china-services-xiaomi)`
- decision: `prefer-reject` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Reject rules take precedence over ordinary direct or proxy rules.)

### 255. semantic-overlap / host-inside-host-suffix
- left: `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miav-cse.avlyun.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miav-cse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 256. semantic-overlap / host-inside-host-suffix
- left: `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui-fxcse.avlyun.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,miui-fxcse.avlyun.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 257. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,hm.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hm.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 258. semantic-overlap / host-inside-host-suffix
- left: `HOST,hm.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hm.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 259. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,hmma.baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hmma.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 260. semantic-overlap / host-inside-host-suffix
- left: `HOST,hmma.baidu.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,baidu.com -> direct (magicrule-china-services-baidu)`
- decision: `ordered-overlap` -> `HOST,hmma.baidu.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 261. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,data.mistat.xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 262. semantic-overlap / host-inside-host-suffix
- left: `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,data.mistat.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 263. semantic-overlap / host-inside-host-suffix
- left: `HOST,flash.sec.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,flash.sec.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 264. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.intl.miui.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,miui.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,tracking.intl.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 265. semantic-overlap / host-inside-host-suffix
- left: `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,a0.app.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 266. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,xiaomi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,api.installer.xiaomi.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 267. semantic-overlap / host-inside-host-suffix
- left: `HOST,safebrowsing.urlsec.qq.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,qq.com -> direct (magicrule-china-services-tencent)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.urlsec.qq.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 268. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,miui.com -> direct (magicrule-china-services-xiaomi)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ china-direct

### 269. semantic-overlap / host-inside-host-suffix
- left: `HOST,tracking.miui.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tracking.miui.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## privacy ↔ proxy

### 270. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)`
- right: `HOST-SUFFIX,linkedin.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.linkedin.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 271. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 272. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

### 273. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis-cn.com -> reject (rulego-tracking)` (Both rules are retained. Reject rules take precedence over ordinary direct or proxy rules.)

## ai ↔ tiktok

### 274. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (magicrule-tiktok)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

## ai ↔ developer

### 275. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grazie.ai -> 全球加速 (magicrule-developer-jetbrains)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,grazie.ai -> 全球加速 (magicrule-developer-jetbrains)` (An explicit value-category override applies to this exact conflict.)

### 276. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,grazie.aws.intellij.net -> 全球加速 (magicrule-developer-jetbrains)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (An explicit value-category override applies to this exact conflict.)

### 277. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jetbrains.ai -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,jetbrains.ai -> 全球加速 (magicrule-developer-jetbrains)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,jetbrains.ai -> 全球加速 (magicrule-developer-jetbrains)` (An explicit value-category override applies to this exact conflict.)

### 278. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,intellij.net -> 全球加速 (magicrule-developer-jetbrains)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,grazie.aws.intellij.net -> AI (acl4ssr-ai)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## ai ↔ github

### 279. exact-policy / same-rule-different-policy
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-proxy.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-value-category` -> `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)` (An explicit value-category override applies to this exact conflict.)

### 280. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-value-category` -> `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)` (An explicit value-category override applies to this exact conflict.)

### 281. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-value-category` -> `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)` (An explicit value-category override applies to this exact conflict.)

### 282. exact-policy / same-rule-different-policy
- left: `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)`
- decision: `prefer-value-category` -> `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)` (An explicit value-category override applies to this exact conflict.)

### 283. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (magicrule-github)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)` (An explicit value-category override applies to this exact conflict.)

### 284. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 285. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 286. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 287. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubnext.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubnext.com -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 288. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 289. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 290. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 291. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 292. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 293. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 294. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ apple

### 295. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-value-category` -> `HOST,apple-relay.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 296. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-value-category` -> `HOST,apple-relay.fastly-edge.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 297. exact-policy / same-rule-different-policy
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-value-category` -> `HOST,gspe1-ssl.ls.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 298. exact-policy / same-rule-different-policy
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,guzzoni.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-value-category` -> `HOST,guzzoni.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 299. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apps.mzstatic.com -> 苹果服务 (magicrule-apple)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,apps.mzstatic.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 300. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 301. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,guzzoni.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,guzzoni.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 302. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 303. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,ls.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ls.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 304. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe1-ssl.ls.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 305. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 306. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.mzstatic.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,apps.mzstatic.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 307. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 308. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 309. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apps.mzstatic.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,mzstatic.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mzstatic.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 310. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## ai ↔ social

### 311. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,grok.com -> 全球加速 (magicrule-social-twitter)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,grok.com -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 312. semantic-overlap / host-inside-host-suffix
- left: `HOST,imagine.meta.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.com -> 全球加速 (magicrule-social-facebook)`
- decision: `ordered-overlap` -> `HOST,imagine.meta.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ google

### 313. exact-policy / same-rule-different-policy
- left: `HOST,ai.google.dev -> AI (magicrule-gemini)`
- right: `HOST,ai.google.dev -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,ai.google.dev -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 314. exact-policy / same-rule-different-policy
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST,alkalicore-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 315. exact-policy / same-rule-different-policy
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 316. exact-policy / same-rule-different-policy
- left: `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,antigravity-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 317. exact-policy / same-rule-different-policy
- left: `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,antigravity.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 318. exact-policy / same-rule-different-policy
- left: `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)`
- right: `HOST,appsgenaiserver-pa.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 319. exact-policy / same-rule-different-policy
- left: `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST,appsgenaiserver-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 320. exact-policy / same-rule-different-policy
- left: `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,appsgenaiserver-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 321. exact-policy / same-rule-different-policy
- left: `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,cloudaicompanion.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 322. exact-policy / same-rule-different-policy
- left: `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 323. exact-policy / same-rule-different-policy
- left: `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,daily-cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 324. exact-policy / same-rule-different-policy
- left: `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)`
- right: `HOST,geminiweb-pa.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 325. exact-policy / same-rule-different-policy
- left: `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST,geminiweb-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 326. exact-policy / same-rule-different-policy
- left: `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,notebooklm-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 327. exact-policy / same-rule-different-policy
- left: `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST,notebooklm.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 328. exact-policy / same-rule-different-policy
- left: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 329. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ai.studio -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,ai.studio -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,ai.studio -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 330. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,aicode.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 331. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,aida.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 332. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 333. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,aistudio.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 334. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,antigravity-unleash.goog -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,antigravity-unleash.goog -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,antigravity-unleash.goog -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 335. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,antigravity.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 336. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,bard.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 337. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,deepmind.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 338. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,deepmind.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 339. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,flow.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 340. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,flow.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 341. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 342. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,gemini.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 343. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,gemini.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 344. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gemini.gstatic.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,gemini.gstatic.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,gemini.gstatic.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 345. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,generativeai.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 346. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 347. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,jules.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 348. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,jules.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 349. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,labs.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 350. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,labs.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 351. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 352. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,makersuite.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 353. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,notebook.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 354. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,notebook.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 355. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,notebooklm.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 356. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 357. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,opal.google -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 358. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,opal.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 359. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 360. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 361. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,stitch.withgoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)` (The configured business-category priority applies to this exact conflict.)

### 362. semantic-overlap / host-inside-host-suffix
- left: `HOST,ai.google.dev -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 363. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 364. semantic-overlap / host-inside-host-suffix
- left: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 365. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 366. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 367. semantic-overlap / host-inside-host-suffix
- left: `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 368. semantic-overlap / host-inside-host-suffix
- left: `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 369. semantic-overlap / host-inside-host-suffix
- left: `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 370. semantic-overlap / host-inside-host-suffix
- left: `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 371. semantic-overlap / host-inside-host-suffix
- left: `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 372. semantic-overlap / host-inside-host-suffix
- left: `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 373. semantic-overlap / host-inside-host-suffix
- left: `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 374. semantic-overlap / host-inside-host-suffix
- left: `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 375. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,makersuite.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 376. semantic-overlap / host-inside-host-suffix
- left: `HOST,makersuite.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 377. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 378. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 379. semantic-overlap / host-inside-host-suffix
- left: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 380. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,aistudio.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 381. semantic-overlap / host-inside-host-suffix
- left: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 382. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,antigravity.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 383. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 384. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity-unleash.goog -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,antigravity-unleash.goog -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity-unleash.goog -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 385. semantic-overlap / host-inside-host-suffix
- left: `HOST,antigravity-unleash.goog -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,goog -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity-unleash.goog -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 386. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,bard.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 387. semantic-overlap / host-inside-host-suffix
- left: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 388. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,gemini.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 389. semantic-overlap / host-inside-host-suffix
- left: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 390. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 391. semantic-overlap / host-inside-host-suffix
- left: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 392. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 393. semantic-overlap / host-inside-host-suffix
- left: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 394. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 395. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 396. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 397. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 398. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,antigravity-unleash.goog -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,goog -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,antigravity-unleash.goog -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 399. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 400. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 401. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 402. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 403. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 404. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 405. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 406. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 407. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 408. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gemini.gstatic.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,gstatic.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.gstatic.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 409. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 410. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 411. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 412. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 413. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 414. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 415. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 416. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 417. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 418. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 419. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 420. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 421. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 422. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 423. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 424. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 425. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 426. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,generativelanguage -> AI (magicrule-gemini)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 427. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST,notebooklm.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 428. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,notebooklm.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 429. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 430. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 431. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,labs.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 432. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,labs.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 433. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 434. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,ai.google.dev -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 435. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 436. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 437. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 438. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 439. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 440. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 441. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 442. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 443. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 444. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 445. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 446. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 447. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,makersuite.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 448. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 449. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 450. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 451. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 452. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 453. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 454. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 455. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 456. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 457. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 458. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 459. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 460. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 461. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 462. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 463. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 464. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 465. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 466. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 467. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 468. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 469. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 470. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 471. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 472. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 473. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 474. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 475. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 476. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 477. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 478. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 479. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 480. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 481. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 482. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 483. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 484. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 485. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 486. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ microsoft

### 487. exact-policy / same-rule-different-policy
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 488. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 489. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 490. exact-policy / same-rule-different-policy
- left: `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)`
- right: `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 491. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (The configured business-category priority applies to this exact conflict.)

### 492. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 493. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubcopilot.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubcopilot.com -> AI (magicrule-copilot)` (The configured business-category priority applies to this exact conflict.)

### 494. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiapi-site.azureedge.net -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaiapi-site.azureedge.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 495. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaiassets.blob.core.windows.net -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaiassets.blob.core.windows.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 496. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,azurefd.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 497. semantic-overlap / host-inside-host-suffix
- left: `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,openaicomproductionae4b.blob.core.windows.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 498. semantic-overlap / host-inside-host-suffix
- left: `HOST,production-openaicom-storage.azureedge.net -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,azureedge.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,production-openaicom-storage.azureedge.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 499. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 500. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry-service.githubusercontent.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 501. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry.githubusercontent.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 502. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,githubnext.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-workspace.githubnext.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 503. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoft.net -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,microsoft.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 504. semantic-overlap / host-inside-host-suffix
- left: `HOST,gateway.bingviz.microsoftapp.net -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 505. semantic-overlap / host-inside-host-suffix
- left: `HOST,sydney.bing.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,bing.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,sydney.bing.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 506. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 507. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 508. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,githubcopilot.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,api.githubcopilot.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 509. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,azure.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ai.azure.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 510. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,api.microsoftapp.net -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,microsoftapp.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 511. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azureedge.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (magicrule-openai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,openaiapi-site.azureedge.net -> AI (magicrule-openai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 512. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,microsoft-falcon.io -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 513. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,bing.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,edgeservices.bing.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,edgeservices.bing.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 514. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- right: `HOST-SUFFIX,microsoft -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 515. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 516. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST,gateway.bingviz.microsoft.net -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoft.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 517. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST,gateway.bingviz.microsoftapp.net -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST,gateway.bingviz.microsoftapp.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 518. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,api.microsoftapp.net -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,api.microsoftapp.net -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 519. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bing-shopping.microsoft-falcon.io -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 520. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 521. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 522. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.cloud.microsoft -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## ai ↔ global-media

### 523. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> AI (rulego-ai-supplement)` (The configured business-category priority applies to this exact conflict.)

## ai ↔ proxy

### 524. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,perplexity.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,perplexity.ai -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 525. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,meta.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,meta.ai -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 526. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,chatgpt.com -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,chatgpt.com -> AI (magicrule-openai)` (An explicit value-category override applies to this exact conflict.)

### 527. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,openai.com -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,openai.com -> AI (magicrule-openai)` (An explicit value-category override applies to this exact conflict.)

### 528. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,x.ai -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,x.ai -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 529. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,smoot.apple.com -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 530. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple-relay.apple.com -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 531. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple-relay.cloudflare.com -> 全球加速 (rulego-proxy)` (An explicit value-category override applies to this exact conflict.)

### 532. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> AI (rulego-ai-supplement)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)` (An explicit value-category override applies to this exact conflict.)

### 533. exact-policy / same-rule-different-policy
- left: `HOST,cp4.cloudflare.com -> AI (rulego-ai-supplement)`
- right: `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,cp4.cloudflare.com -> 全球加速 (rulego-proxy)` (An explicit value-category override applies to this exact conflict.)

### 534. exact-policy / same-rule-different-policy
- left: `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)`
- right: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,copilot.microsoft.com -> AI (rulego-ai-supplement)` (An explicit value-category override applies to this exact conflict.)

### 535. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,civitai.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,civitai.com -> AI (local-civitai-1)`
- decision: `prefer-category` -> `HOST-SUFFIX,civitai.com -> AI (local-civitai-1)` (The configured business-category priority applies to this exact conflict.)

### 536. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot.microsoft.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,copilot.microsoft.com -> AI (magicrule-copilot)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 537. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,chatgpt -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,chatgpt.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,chatgpt -> AI (magicrule-openai)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 538. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,openai -> AI (magicrule-openai)`
- right: `HOST-SUFFIX,openai.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,openai -> AI (magicrule-openai)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 539. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,notebooklm.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 540. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,labs.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 541. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 542. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 543. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 544. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,antigravity-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 545. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,antigravity.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 546. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 547. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 548. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 549. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,cloudaicompanion.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 550. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 551. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,daily-cloudcode-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 552. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 553. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 554. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,makersuite.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 555. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,notebooklm-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 556. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,notebooklm.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 557. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 558. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aicode.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 559. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aida.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 560. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aisandbox-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 561. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aistudio.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 562. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,antigravity.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 563. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apis.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 564. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 565. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 566. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 567. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 568. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 569. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 570. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 571. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 572. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 573. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 574. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 575. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 576. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 577. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labstailwind.pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 578. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 579. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 580. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 581. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 582. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 583. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 584. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 585. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 586. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 587. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,stitch.withgoogle.com -> AI (magicrule-gemini)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 588. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,aistudio.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,aistudio.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 589. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.google -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,antigravity.google -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 590. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,bard.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,bard.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 591. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gemini.google.com -> AI (rulego-ai-supplement)`
- decision: `ordered-overlap` -> `HOST,gemini.google.com -> AI (rulego-ai-supplement)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 592. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,generativelanguage.googleapis.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 593. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.google.com -> AI (acl4ssr-ai)`
- decision: `ordered-overlap` -> `HOST,notebooklm.google.com -> AI (acl4ssr-ai)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google-voice ↔ google

### 594. exact-policy / same-rule-different-policy
- left: `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)` (The configured business-category priority applies to this exact conflict.)

### 595. semantic-overlap / host-inside-host-suffix
- left: `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 596. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google-voice ↔ proxy

### 597. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 美国节点 (magicrule-google-voice)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## youtube ↔ google

### 598. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 599. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 600. semantic-overlap / host-inside-host-suffix
- left: `HOST,beacons.gcp.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,beacons.gcp.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 601. semantic-overlap / host-inside-host-suffix
- left: `HOST,beacons.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,beacons.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 602. semantic-overlap / host-inside-host-suffix
- left: `HOST,beacons2.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,beacons2.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 603. semantic-overlap / host-inside-host-suffix
- left: `HOST,beacons3.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,beacons3.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 604. semantic-overlap / host-inside-host-suffix
- left: `HOST,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 605. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 606. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 607. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 608. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 609. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gcp.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacons.gcp.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 610. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacons.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 611. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacons2.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 612. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,beacons3.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 613. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 614. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt2.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gcp.gvt2.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 615. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 616. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 617. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 618. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 619. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 620. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 621. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 622. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 623. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 624. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 625. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 628. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 629. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 631. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 632. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 633. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## youtube ↔ global-media

### 634. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 635. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,withyoutube.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,withyoutube.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 636. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtu.be -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtu.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,youtu.be -> YouTube (magicrule-youtube)` (The configured business-category priority applies to this exact conflict.)

### 637. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,youtube.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 638. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubeeducation.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,youtubeeducation.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 639. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubegaming.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,youtubegaming.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 640. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtubekids.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,youtubekids.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 641. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,youtube-nocookie.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,youtube-nocookie.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 642. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,yt.be -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,yt.be -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,yt.be -> YouTube (magicrule-youtube)` (The configured business-category priority applies to this exact conflict.)

### 643. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ytimg.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,ytimg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ytimg.com -> YouTube (magicrule-youtube)` (The configured business-category priority applies to this exact conflict.)

### 644. exact-policy / same-rule-different-policy
- left: `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 645. exact-policy / same-rule-different-policy
- left: `HOST,yt3.ggpht.com -> YouTube (magicrule-youtube)`
- right: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST,yt3.ggpht.com -> YouTube (magicrule-youtube)` (An explicit value-category override applies to this exact conflict.)

### 646. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 647. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,yt3.ggpht.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,yt3.ggpht.com -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 648. semantic-overlap / host-inside-host-suffix
- left: `HOST,yt3.ggpht.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,ggpht.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggpht.com -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 649. semantic-overlap / host-inside-host-suffix
- left: `HOST,music.youtube.com -> YouTube (magicrule-youtube-music)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,music.youtube.com -> YouTube (magicrule-youtube-music)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 650. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ads.youtube.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ads.youtube.com -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 651. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,withyoutube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 652. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 653. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubeeducation.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 654. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubegaming.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 655. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtubekids.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 656. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube-nocookie.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 657. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,youtube -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 658. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,youtube.* -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,youtube.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,youtube.* -> YouTube (magicrule-youtube)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## youtube ↔ proxy

### 659. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt1.com -> YouTube (magicrule-youtube)` (The configured business-category priority applies to this exact conflict.)

### 660. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 661. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST,yt3.googleusercontent.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 662. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 663. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,video.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 664. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wide-youtube.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 665. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube-ui.l.google.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 666. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtube.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 667. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubeembeddedplayer.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 668. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,youtubei.googleapis.com -> YouTube (magicrule-youtube)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ social

### 669. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.226.106.180/32 -> Netflix (magicrule-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (magicrule-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.226.106.180/32 -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 670. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.114.205/32 -> Netflix (magicrule-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (magicrule-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.231.114.205/32 -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 671. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,34.231.213.21/32 -> Netflix (magicrule-netflix)`
- right: `IP-CIDR,34.224.0.0/12 -> 全球加速 (magicrule-social-whatsapp)`
- decision: `ordered-overlap` -> `IP-CIDR,34.231.213.21/32 -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ microsoft

### 672. semantic-overlap / host-inside-host-suffix
- left: `HOST,netflix.com.edgesuite.net -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,netflix.com.edgesuite.net -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 673. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflix.com.edgesuite.net -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## netflix ↔ global-media

### 674. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,fast.com -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,fast.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,fast.com -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 675. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.com -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,netflix.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,netflix.com -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 676. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,netflix.net -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,netflix.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,netflix.net -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 677. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxext.com -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,nflxext.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,nflxext.com -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 678. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.com -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,nflximg.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,nflximg.com -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 679. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflximg.net -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,nflximg.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,nflximg.net -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 680. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxso.net -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,nflxso.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,nflxso.net -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 681. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,nflxvideo.net -> Netflix (magicrule-netflix)`
- right: `HOST-SUFFIX,nflxvideo.net -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,nflxvideo.net -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 682. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,netflixdnstest -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 683. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 684. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (magicrule-netflix)` (The configured business-category priority applies to this exact conflict.)

### 685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,apiproxy-device-prod-nlb- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,apiproxy-device-prod-nlb- -> Netflix (magicrule-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 686. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,dualstack.apiproxy- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,dualstack.apiproxy- -> Netflix (magicrule-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> Netflix (magicrule-netflix)`
- right: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,netflixdnstest -> Netflix (magicrule-netflix)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest0.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest0.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest1.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest1.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest10.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest10.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 691. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest2.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest2.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 692. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest3.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest3.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 693. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest4.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest4.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 694. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest5.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest5.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 695. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest6.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest6.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 696. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest7.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest7.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 697. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest8.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest8.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 698. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,netflixdnstest9.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,netflixdnstest9.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 699. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,netflixdnstest -> 国际媒体 (rulego-global-media)`
- right: `HOST-WILDCARD,netflixdnstest*.com -> Netflix (magicrule-netflix)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,netflixdnstest*.com -> Netflix (magicrule-netflix)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## tiktok ↔ microsoft

### 700. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,tiktokcdn-us.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-us.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 701. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,tiktokcdn.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 702. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,tiktokv.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokv.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## tiktok ↔ global-media

### 703. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,byteoversea.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,byteoversea.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,byteoversea.com -> 海外抖音 (magicrule-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 704. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,ibytedtos.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ibytedtos.com -> 海外抖音 (magicrule-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 705. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,muscdn.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,muscdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,muscdn.com -> 海外抖音 (magicrule-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 706. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,musical.ly -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,musical.ly -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

### 707. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktok.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,tiktok.com -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

### 708. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tik-tokapi.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,tik-tokapi.com -> 海外抖音 (magicrule-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 709. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,tiktokcdn.com -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

### 710. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokcdn-eu.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,tiktokcdn-eu.com -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

### 711. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tiktokv.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,tiktokv.com -> 海外抖音 (magicrule-tiktok)` (An explicit value-category override applies to this exact conflict.)

### 712. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ttwstatic.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,ttwstatic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,ttwstatic.com -> 海外抖音 (magicrule-tiktok)` (The configured business-category priority applies to this exact conflict.)

### 713. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,analytics.tiktok.com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,analytics.tiktok.com -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 714. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-tiktokcdn-com -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,-tiktokcdn-com -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 715. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,musical.ly -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,musical.ly -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,musical.ly -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 716. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktok.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 717. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 718. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 719. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokv.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 720. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktok -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 721. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 722. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 723. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)`
- right: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,tiktokcdn -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST,p16-tiktokcdn-com.akamaized.net -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-eu.com -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-eu.com -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-us.com -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,tiktokcdn- -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tiktokcdn-us.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tiktokcdn-us.com.edgesuite.net -> 海外抖音 (magicrule-tiktok)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## telegram ↔ social

### 728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,instanttelegram.com -> 全球加速 (magicrule-social-facebook)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,instanttelegram.com -> 全球加速 (magicrule-social-facebook)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## telegram ↔ proxy

### 729. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,cdn-telegram.org -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 730. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,comments.app -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,comments.app -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,comments.app -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 731. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,graph.org -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,graph.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,graph.org -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 732. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,legra.ph -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,legra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,legra.ph -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 733. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,quiz.directory -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,quiz.directory -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,quiz.directory -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 734. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,t.me -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,t.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,t.me -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 735. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tdesktop.com -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,tdesktop.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tdesktop.com -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 736. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegra.ph -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegra.ph -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegra.ph -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 737. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.dog -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.dog -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 738. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.me -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.me -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 739. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.org -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.org -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 740. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram.space -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram.space -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 741. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telegram-cdn.org -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 742. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,telesco.pe -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telesco.pe -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,telesco.pe -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 743. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tg.dev -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,tg.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tg.dev -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 744. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tx.me -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,tx.me -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,tx.me -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 745. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.56.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.56.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 746. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.4.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.4.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 747. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.8.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.8.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 748. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.16.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.16.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 749. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.12.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.12.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 750. exact-policy / same-rule-different-policy
- left: `IP-CIDR,149.154.160.0/20 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,149.154.160.0/20 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 751. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.105.192.0/23 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.105.192.0/23 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.105.192.0/23 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 752. exact-policy / same-rule-different-policy
- left: `IP-CIDR,91.108.20.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,91.108.20.0/22 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 753. exact-policy / same-rule-different-policy
- left: `IP-CIDR,185.76.151.0/24 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,185.76.151.0/24 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP-CIDR,185.76.151.0/24 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 754. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23d::/48 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23d::/48 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 755. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:b28:f23f::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23f::/48 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 756. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:67c:4e8::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:67c:4e8::/48 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 757. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2001:b28:f23c::/48 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2001:b28:f23c::/48 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 758. exact-policy / same-rule-different-policy
- left: `IP6-CIDR,2a0a:f280::/32 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `IP6-CIDR,2a0a:f280::/32 -> 电报代理 (magicrule-telegram)` (The configured business-category priority applies to this exact conflict.)

### 759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cdn-telegram.org -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,telegram.dog -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,telegram.me -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,telegram.org -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,telegram.space -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,telegram -> 电报代理 (magicrule-telegram)`
- right: `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,telegram-cdn.org -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 765. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,149.154.160.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,149.154.160.0/22 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 766. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,149.154.164.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,149.154.164.0/22 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 767. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,149.154.168.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,149.154.168.0/22 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 768. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,149.154.172.0/22 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,149.154.160.0/20 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,149.154.172.0/22 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 769. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 770. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.4.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 771. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 772. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 773. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 774. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.0.0/16 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 775. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.16.0/21 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.16.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 776. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.16.0/21 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 777. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.20.0/23 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.20.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.20.0/23 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 778. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.56.0/23 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.56.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.56.0/23 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 779. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.8.0/21 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.8.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 780. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,91.108.8.0/21 -> 电报代理 (magicrule-telegram)`
- right: `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP-CIDR,91.108.12.0/22 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 781. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23d::/48 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 782. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2001:b28:f23c::/47 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2001:b28:f23c::/48 -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 783. semantic-overlap / ip-cidr-overlap
- left: `IP6-CIDR,2a0a:f280:203::/48 -> 电报代理 (magicrule-telegram)`
- right: `IP6-CIDR,2a0a:f280::/32 -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `IP6-CIDR,2a0a:f280:203::/48 -> 电报代理 (magicrule-telegram)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## spotify ↔ microsoft

### 784. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,spotify.com.edgesuite.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com.edgesuite.net -> Spotify (magicrule-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## spotify ↔ global-media

### 785. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,pscdn.co -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,pscdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,pscdn.co -> Spotify (magicrule-spotify)` (The configured business-category priority applies to this exact conflict.)

### 786. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,scdn.co -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,scdn.co -> Spotify (magicrule-spotify)` (The configured business-category priority applies to this exact conflict.)

### 787. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,spotify.com -> Spotify (magicrule-spotify)` (An explicit value-category override applies to this exact conflict.)

### 788. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,spoti.fi -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spoti.fi -> 国际媒体 (rulego-global-media)`
- decision: `prefer-category` -> `HOST-SUFFIX,spoti.fi -> Spotify (magicrule-spotify)` (The configured business-category priority applies to this exact conflict.)

### 789. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)` (An explicit value-category override applies to this exact conflict.)

### 790. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,-spotify-com -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-KEYWORD,-spotify-com -> Spotify (magicrule-spotify)` (An explicit value-category override applies to this exact conflict.)

### 791. semantic-overlap / host-inside-host-suffix
- left: `HOST,adeventtracker.spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,adeventtracker.spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 792. semantic-overlap / host-inside-host-suffix
- left: `HOST,adstudio-assets.scdn.co -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,scdn.co -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,adstudio-assets.scdn.co -> Spotify (magicrule-spotify)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 793. semantic-overlap / host-inside-host-suffix
- left: `HOST,bloodhound.spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,bloodhound.spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 794. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify- -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,-spotify- -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 795. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,-spotify-com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 796. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 797. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 798. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 799. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-SUFFIX,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 800. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)`
- right: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 801. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,adeventtracker.spotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,adeventtracker.spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 802. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,bloodhound.spotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,bloodhound.spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 803. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,byspotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,byspotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 804. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,lifeatspotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,lifeatspotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 805. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 806. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,spotify.com.edgesuite.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,spotify.com.edgesuite.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 807. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,spotify.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tospotify.com -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tospotify.com -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 808. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,audio-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 809. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,audio4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 810. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,heads-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 811. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST,heads4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST,heads4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 812. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,audio-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 813. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,-spotify-com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,heads4-ak-spotify-com.akamaized.net -> Spotify (magicrule-spotify)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## developer ↔ global-media

### 814. semantic-overlap / host-inside-host-suffix
- left: `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (magicrule-developer-docker)`
- right: `HOST-SUFFIX,d2wy8f7a9ursnm.cloudfront.net -> 国际媒体 (magicrule-global-media-abema-tv)`
- decision: `ordered-overlap` -> `HOST,d2wy8f7a9ursnm.cloudfront.net -> 全球加速 (magicrule-developer-docker)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## developer ↔ china-services

### 815. semantic-overlap / host-inside-host-suffix
- left: `HOST,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)`
- right: `HOST-SUFFIX,oss-cn-hongkong.aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 816. semantic-overlap / host-inside-host-suffix
- left: `HOST,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)`
- right: `HOST-SUFFIX,aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 817. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- right: `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 818. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)`
- right: `HOST-SUFFIX,oss-cn-hongkong.aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gitlab-assets.oss-cn-hongkong.aliyuncs.com -> 全球加速 (magicrule-developer-gitlab)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ microsoft

### 819. exact-policy / same-rule-different-policy
- left: `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,copilot-proxy.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,copilot-proxy.githubusercontent.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 820. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 821. exact-policy / same-rule-different-policy
- left: `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 822. exact-policy / same-rule-different-policy
- left: `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 823. exact-policy / same-rule-different-policy
- left: `HOST,github-api.arkoselabs.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-api.arkoselabs.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-api.arkoselabs.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 824. exact-policy / same-rule-different-policy
- left: `HOST,github-cloud.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-cloud.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-cloud.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 825. exact-policy / same-rule-different-policy
- left: `HOST,github-production-release-asset-2e65be.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-production-release-asset-2e65be.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-production-release-asset-2e65be.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 826. exact-policy / same-rule-different-policy
- left: `HOST,github-production-repository-file-5c1aeb.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-production-repository-file-5c1aeb.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-production-repository-file-5c1aeb.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 827. exact-policy / same-rule-different-policy
- left: `HOST,github-production-repository-image-32fea6.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-production-repository-image-32fea6.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-production-repository-image-32fea6.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 828. exact-policy / same-rule-different-policy
- left: `HOST,github-production-upload-manifest-file-7fdce7.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-production-upload-manifest-file-7fdce7.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-production-upload-manifest-file-7fdce7.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 829. exact-policy / same-rule-different-policy
- left: `HOST,github-production-user-asset-6210df.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST,github-production-user-asset-6210df.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,github-production-user-asset-6210df.s3.amazonaws.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 830. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa0.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa0.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa0.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 831. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa1.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa1.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa1.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 832. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa10.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa10.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa10.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 833. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa11.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa11.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa11.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 834. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa12.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa12.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa12.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 835. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa13.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa13.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa13.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 836. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa14.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa14.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa14.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 837. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa15.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa15.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa15.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 838. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa16.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa16.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa16.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 839. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa17.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa17.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa17.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 840. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa18.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa18.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa18.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 841. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa19.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa19.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa19.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 842. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa2.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa2.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa2.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 843. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa3.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa3.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa3.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 844. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa4.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa4.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa4.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 845. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa5.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa5.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa5.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 846. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa6.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa6.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa6.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 847. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa7.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa7.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa7.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 848. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa8.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa8.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa8.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 849. exact-policy / same-rule-different-policy
- left: `HOST,productionresultssa9.blob.core.windows.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,productionresultssa9.blob.core.windows.net -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST,productionresultssa9.blob.core.windows.net -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 850. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,atom.io -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,atom.io -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,atom.io -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 851. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,cafe.github.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cafe.github.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,cafe.github.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 852. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,collector.github.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,collector.github.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,collector.github.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 853. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,dependabot.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dependabot.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,dependabot.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 854. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gh.io -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,gh.io -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,gh.io -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 855. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ghcr.io -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,ghcr.io -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,ghcr.io -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 856. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,ghe.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,ghe.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,ghe.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 857. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,git.io -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,git.io -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,git.io -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 858. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.ai -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.ai -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.ai -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 859. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.blog -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.blog -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.blog -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 860. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.career -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.career -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.career -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 861. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 862. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.community -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.community -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.community -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 863. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.dev -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.dev -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.dev -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 864. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,github.io -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.io -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,github.io -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 865. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubapp.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubapp.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubapp.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 866. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubassets.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubassets.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubassets.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 867. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubcopilot.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubcopilot.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubcopilot.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 868. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubhackathon.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubhackathon.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubhackathon.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 869. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubnext.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubnext.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubnext.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 870. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubpreview.dev -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubpreview.dev -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubpreview.dev -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 871. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubstatus.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubstatus.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubstatus.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 872. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubsupport.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubsupport.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubsupport.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 873. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubuniverse.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubuniverse.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubuniverse.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 874. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 875. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,myoctocat.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,myoctocat.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,myoctocat.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 876. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,octocaptcha.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,octocaptcha.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,octocaptcha.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 877. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,opensource.guide -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,opensource.guide -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,opensource.guide -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 878. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,repo.new -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,repo.new -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,repo.new -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 879. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,thegithubshop.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,thegithubshop.com -> GitHub (magicrule-github)`
- decision: `prefer-category` -> `HOST-SUFFIX,thegithubshop.com -> GitHub (magicrule-github)` (The configured business-category priority applies to this exact conflict.)

### 880. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 881. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 882. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry-service.githubusercontent.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 883. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 884. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry.githubusercontent.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 885. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubusercontent.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 886. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubnext.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-workspace.githubnext.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 887. semantic-overlap / host-inside-host-suffix
- left: `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,githubnext.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 888. semantic-overlap / host-inside-host-suffix
- left: `HOST,github-cloud.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github-cloud.s3.amazonaws.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST,github-cloud.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 889. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa0.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa0.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 890. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa1.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa1.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 891. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa10.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa10.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 892. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa11.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa11.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 893. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa12.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa12.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 894. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa13.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa13.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 895. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa14.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa14.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 896. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa15.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa15.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 897. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa16.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa16.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 898. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa17.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa17.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 899. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa18.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa18.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 900. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa19.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa19.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 901. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa2.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa2.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 902. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa3.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa3.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 903. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa4.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa4.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 904. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa5.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa5.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 905. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa6.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa6.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 906. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa7.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa7.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 907. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa8.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa8.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 908. semantic-overlap / host-inside-host-suffix
- left: `HOST,productionresultssa9.blob.core.windows.net -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,windows.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,productionresultssa9.blob.core.windows.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 909. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cafe.github.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cafe.github.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 910. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cafe.github.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cafe.github.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 911. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,collector.github.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,github.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collector.github.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 912. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,collector.github.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collector.github.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 913. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-proxy.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 914. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry-service.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 915. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-telemetry.githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 916. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,copilot-workspace.githubnext.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 917. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-api.arkoselabs.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-api.arkoselabs.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 918. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-cloud.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-cloud.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 919. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-production-release-asset-2e65be.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-production-release-asset-2e65be.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 920. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-production-repository-file-5c1aeb.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-production-repository-file-5c1aeb.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 921. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-production-repository-image-32fea6.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-production-repository-image-32fea6.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 922. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-production-upload-manifest-file-7fdce7.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-production-upload-manifest-file-7fdce7.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github-production-user-asset-6210df.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,github-production-user-asset-6210df.s3.amazonaws.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 924. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,cafe.github.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cafe.github.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 925. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,collector.github.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collector.github.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 926. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.ai -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.ai -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 927. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.blog -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.blog -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 928. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.career -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.career -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 929. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 930. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.community -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.community -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 931. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.dev -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.dev -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 932. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,github.io -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github.io -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 933. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubapp.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubapp.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 934. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubassets.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubassets.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 935. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubcopilot.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubcopilot.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 936. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubhackathon.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubhackathon.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 937. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubnext.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubnext.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 938. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubpreview.dev -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubpreview.dev -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 939. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubstatus.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubstatus.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 940. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubsupport.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubsupport.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 941. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubuniverse.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubuniverse.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 942. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,githubusercontent.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 943. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,thegithubshop.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thegithubshop.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ china-services

### 944. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- right: `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 945. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (magicrule-github)`
- right: `HOST-SUFFIX,oss-cn-hongkong.aliyuncs.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-avatars.oss-cn-hongkong.aliyuncs.com -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## github ↔ proxy

### 946. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,freetls.fastly.net -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (magicrule-github)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,github-atom-io-herokuapp-com.freetls.fastly.net -> GitHub (magicrule-github)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 947. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,github -> GitHub (magicrule-github)`
- right: `HOST,github.global.ssl.fastly.net -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,github -> GitHub (magicrule-github)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## apple ↔ google

### 948. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (magicrule-google)`
- decision: `prefer-category` -> `HOST-SUFFIX,crashlytics.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 949. semantic-overlap / host-inside-host-suffix
- left: `HOST,firebase-settings.crashlytics.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST,firebase-settings.crashlytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 950. semantic-overlap / host-inside-host-suffix
- left: `HOST,update.crashlytics.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST,update.crashlytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 951. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,firebase-settings.crashlytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,firebase-settings.crashlytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 952. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,crashlytics.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,update.crashlytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,update.crashlytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ microsoft

### 953. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-category` -> `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 954. semantic-overlap / host-inside-host-suffix
- left: `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,adcdownload.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 955. semantic-overlap / host-inside-host-suffix
- left: `HOST,amp-api-edge-lb-cn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,amp-api-edge-lb-cn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 956. semantic-overlap / host-inside-host-suffix
- left: `HOST,amp-api-edge-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,amp-api-edge-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 957. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 958. semantic-overlap / host-inside-host-suffix
- left: `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 959. semantic-overlap / host-inside-host-suffix
- left: `HOST,cds.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cds.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 960. semantic-overlap / host-inside-host-suffix
- left: `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,certs-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 961. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 962. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl2-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl2-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 963. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl2.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl2.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 964. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 965. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 966. semantic-overlap / host-inside-host-suffix
- left: `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 967. semantic-overlap / host-inside-host-suffix
- left: `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,clientflow.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 968. semantic-overlap / host-inside-host-suffix
- left: `HOST,configuration-lb.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,configuration-lb.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 969. semantic-overlap / host-inside-host-suffix
- left: `HOST,configuration.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,configuration.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 970. semantic-overlap / host-inside-host-suffix
- left: `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,crl-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 971. semantic-overlap / host-inside-host-suffix
- left: `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 972. semantic-overlap / host-inside-host-suffix
- left: `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 973. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 974. semantic-overlap / host-inside-host-suffix
- left: `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 975. semantic-overlap / host-inside-host-suffix
- left: `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 976. semantic-overlap / host-inside-host-suffix
- left: `HOST,inappcheck-cn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,inappcheck-cn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 977. semantic-overlap / host-inside-host-suffix
- left: `HOST,inappcheck-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,inappcheck-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 978. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 979. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 980. semantic-overlap / host-inside-host-suffix
- left: `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 981. semantic-overlap / host-inside-host-suffix
- left: `HOST,init.gc-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,init.gc-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 982. semantic-overlap / host-inside-host-suffix
- left: `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 983. semantic-overlap / host-inside-host-suffix
- left: `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 984. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 985. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,mesu-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 986. semantic-overlap / host-inside-host-suffix
- left: `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,mesu-china.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 987. semantic-overlap / host-inside-host-suffix
- left: `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,oscdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 988. semantic-overlap / host-inside-host-suffix
- left: `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,prod-support.apple-support.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 989. semantic-overlap / host-inside-host-suffix
- left: `HOST,push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 990. semantic-overlap / host-inside-host-suffix
- left: `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 991. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 992. semantic-overlap / host-inside-host-suffix
- left: `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,store.storeimages.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 993. semantic-overlap / host-inside-host-suffix
- left: `HOST,support-china.apple-support.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,support-china.apple-support.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 994. semantic-overlap / host-inside-host-suffix
- left: `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 995. semantic-overlap / host-inside-host-suffix
- left: `HOST,swdist.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,swdist.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 996. semantic-overlap / host-inside-host-suffix
- left: `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,swscan-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 997. semantic-overlap / host-inside-host-suffix
- left: `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 998. semantic-overlap / host-inside-host-suffix
- left: `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,valid.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 999. semantic-overlap / host-inside-host-suffix
- left: `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,weather-data.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1000. semantic-overlap / host-inside-host-suffix
- left: `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,www-cdn.icloud.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1001. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1002. semantic-overlap / host-inside-host-suffix
- left: `HOST,e16991.b.akamaiedge.net -> 苹果服务 (local-alias-e16991-b-akamaiedge-net)`
- right: `HOST-SUFFIX,b.akamaiedge.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,e16991.b.akamaiedge.net -> 苹果服务 (local-alias-e16991-b-akamaiedge-net)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1003. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,adcdownload.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adcdownload.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1004. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,apple-support.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple-support.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1005. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1006. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1007. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bag-cdn.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1008. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1009. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cds.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cds.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1010. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cl1-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1011. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cl2.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cl2.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1012. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cl3-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1013. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cl4-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1014. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cl5-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1015. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,clientflow.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,clientflow.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1016. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,configuration.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,configuration.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1017. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,courier-push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,courier-push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1018. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dd-cdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1019. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gsp4-cn.ls.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1020. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gspe19-2-cn-ssl.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1021. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gspe19-cn.ls-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1022. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,icloud.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,icloud.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1023. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,images.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1024. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,init-p01md-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1025. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,init-p01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1026. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,init-s01st-lb.push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1027. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,iphone-ld.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1028. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,is-ssl.mzstatic.com-cn-lb.itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1029. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,isu.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,isu.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1030. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1031. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,live.com.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,live.com.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1032. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mail.me.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mail.me.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1033. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mesu-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mesu-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1034. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mesu-china.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mesu-china.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1035. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,microsoft.com.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,microsoft.com.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1036. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,oaspapps.com.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oaspapps.com.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1037. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,onecollector.cloudapp.aria.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,onecollector.cloudapp.aria.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1038. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1039. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oscdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oscdn.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1040. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,prod-support.apple-support.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,prod-support.apple-support.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1041. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,push-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1042. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,skype-edf.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,skype-edf.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1043. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,skypedata.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,skypedata.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1044. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,stocks-sparkline-lb.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1045. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,store.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1046. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,store.storeimages.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,store.storeimages.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1047. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,support-china.apple-support.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,support-china.apple-support.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1048. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,swcatalog-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1049. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,swdist.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,swdist.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1050. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,swscan-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,swscan-cdn.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1051. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,updates-http.cdn-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1052. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,valid.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,valid.origin-apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1053. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,weather-data.apple.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,weather-data.apple.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1054. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,windows.com.akadns.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,windows.com.akadns.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1055. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,www-cdn.icloud.com.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,www-cdn.icloud.com.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1056. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,akadns.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,www.apple.com.edgekey.net.globalredir.akadns.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1057. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,appldnld.apple.com.edgesuite.net -> 苹果服务 (magicrule-apple)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1058. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (local-alias-ls-apple-com-edgesuite-net)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ls.apple.com.edgesuite.net -> 苹果服务 (local-alias-ls-apple-com-edgesuite-net)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## apple ↔ global-media

### 1059. exact-policy / same-rule-different-policy
- left: `HOST,tv.applemusic.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST,tv.applemusic.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1060. exact-policy / same-rule-different-policy
- left: `HOST,play-edge.itunes.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST,play-edge.itunes.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1061. exact-policy / same-rule-different-policy
- left: `HOST,uts-api.itunes.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST,uts-api.itunes.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1062. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play-edge.itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1063. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1064. semantic-overlap / host-inside-host-suffix
- left: `HOST,play-edge.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1065. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.applemusic.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,applemusic.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,applemusic.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1066. semantic-overlap / host-inside-host-suffix
- left: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1067. semantic-overlap / host-inside-host-suffix
- left: `HOST,uts-api.itunes.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1068. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tv.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1069. semantic-overlap / host-inside-host-suffix
- left: `HOST,linear.tv.apple.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## apple ↔ china-direct

### 1070. semantic-overlap / host-inside-host-suffix
- left: `HOST,captive.apple.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1071. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,lcdn-locator.apple.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## apple ↔ proxy

### 1072. exact-policy / same-rule-different-policy
- left: `HOST,testflight.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,testflight.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1073. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appsto.re -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,appsto.re -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,appsto.re -> 苹果服务 (magicrule-apple)` (The configured business-category priority applies to this exact conflict.)

### 1074. exact-policy / same-rule-different-policy
- left: `HOST,books.itunes.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,books.itunes.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1075. exact-policy / same-rule-different-policy
- left: `HOST,lookup-api.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,lookup-api.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1076. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple-relay.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1077. exact-policy / same-rule-different-policy
- left: `HOST,apple-relay.fastly-edge.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,apple-relay.fastly-edge.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple-relay.fastly-edge.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1078. exact-policy / same-rule-different-policy
- left: `HOST,apps.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apps.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1079. exact-policy / same-rule-different-policy
- left: `HOST,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,itunes.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1080. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apple.news -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,apple.news -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1081. exact-policy / same-rule-different-policy
- left: `HOST,news-assets.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,news-assets.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1082. exact-policy / same-rule-different-policy
- left: `HOST,news-client.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,news-client.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1083. exact-policy / same-rule-different-policy
- left: `HOST,news-edge.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,news-edge.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1084. exact-policy / same-rule-different-policy
- left: `HOST,news-events.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,news-events.apple.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1085. exact-policy / same-rule-different-policy
- left: `HOST,apple.comscoreresearch.com -> 苹果服务 (magicrule-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,apple.comscoreresearch.com -> 苹果服务 (magicrule-apple)` (An explicit value-category override applies to this exact conflict.)

### 1086. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple-relay.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1087. semantic-overlap / host-inside-host-suffix
- left: `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api-glb-sea.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1088. semantic-overlap / host-inside-host-suffix
- left: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.comscoreresearch.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1089. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apps.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apps.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1090. semantic-overlap / host-inside-host-suffix
- left: `HOST,apps.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1091. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1092. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1093. semantic-overlap / host-inside-host-suffix
- left: `HOST,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1094. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1095. semantic-overlap / host-inside-host-suffix
- left: `HOST,itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1096. semantic-overlap / host-inside-host-suffix
- left: `HOST,lookup-api.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1097. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,news-assets.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1098. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-assets.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1099. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,news-client.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1100. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1101. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,news-edge.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1102. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-edge.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1103. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,news-events.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1104. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-events.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1105. semantic-overlap / host-inside-host-suffix
- left: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1106. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,music.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,music.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1107. semantic-overlap / host-inside-host-suffix
- left: `HOST,beta.music.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1108. semantic-overlap / host-inside-host-suffix
- left: `HOST,facetime.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1109. semantic-overlap / host-inside-host-suffix
- left: `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,radio.itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,radio.itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1110. semantic-overlap / host-inside-host-suffix
- left: `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itunes.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1111. semantic-overlap / host-inside-host-suffix
- left: `HOST,radio.itunes.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1112. semantic-overlap / host-inside-host-suffix
- left: `HOST,books.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1113. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tv.apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tv.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1114. semantic-overlap / host-inside-host-suffix
- left: `HOST,tv.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1115. semantic-overlap / host-inside-host-suffix
- left: `HOST,news-client-search.apple.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1116. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1117. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,smoot.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,guzzoni.smoot.apple.com -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1118. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,testflight -> 苹果服务 (magicrule-apple)`
- right: `HOST,testflight.apple.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,testflight -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1119. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (magicrule-apple)`
- right: `HOST,apple.comscoreresearch.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,apple.* -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1120. semantic-overlap / host-wildcard-overlap
- left: `HOST-WILDCARD,apple.* -> 苹果服务 (magicrule-apple)`
- right: `HOST-SUFFIX,apple.news -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-WILDCARD,apple.* -> 苹果服务 (magicrule-apple)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## social ↔ google

### 1121. semantic-overlap / host-inside-host-suffix
- left: `HOST,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1122. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1123. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,discordapp.page.link -> 全球加速 (magicrule-social-discord)`
- right: `HOST-SUFFIX,page.link -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discordapp.page.link -> 全球加速 (magicrule-social-discord)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1124. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)`
- decision: `ordered-overlap` -> `HOST,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1125. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,discord-attachments-uploads-prd.storage.googleapis.com -> 全球加速 (magicrule-social-discord)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## social ↔ global-media

### 1126. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,linetv.tw -> 全球加速 (magicrule-social-line)`
- right: `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,linetv.tw -> 国际媒体 (rulego-global-media)` (An explicit value-category override applies to this exact conflict.)

## google ↔ microsoft

### 1127. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,tenor.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,tenor.com -> 全球加速 (magicrule-microsoft)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,tenor.com -> 全球加速 (magicrule-microsoft)` (An explicit value-category override applies to this exact conflict.)

## google ↔ global-media

### 1128. semantic-overlap / host-inside-host-suffix
- left: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1129. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1130. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)` (Both rules are retained. An explicit value-category override provides the first-match order.)

## google ↔ china-services

### 1131. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,qingmail.cn -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.cn -> direct (magicrule-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1132. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,gmail -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,qingmail.com -> direct (magicrule-china-services-sina)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qingmail.com -> direct (magicrule-china-services-sina)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ china-direct

### 1133. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt1-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt1-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1134. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt2-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt2-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1135. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt3-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt3-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1136. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt4-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt4-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1137. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt5-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt5-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1138. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt6-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt6-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1139. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt7-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt7-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1140. semantic-overlap / host-inside-host-suffix
- left: `HOST,alt8-mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt8-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1141. semantic-overlap / host-inside-host-suffix
- left: `HOST,mtalk.google.com -> direct (magicrule-google)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1142. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt1-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt1-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1143. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt2-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt2-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1144. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt3-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt3-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1145. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt4-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt4-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1146. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt5-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt5-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1147. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt6-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt6-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1148. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt7-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt7-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1149. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,alt8-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt8-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1150. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST,mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## google ↔ proxy

### 1151. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,apigee.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,apigee.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,apigee.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1152. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,appspot.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,appspot.com -> 谷歌服务 (magicrule-google)` (An explicit value-category override applies to this exact conflict.)

### 1153. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,blogger.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,blogger.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,blogger.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1154. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt0.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt0.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt0.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1155. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,gvt3.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt3.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,gvt3.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1156. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1157. exact-policy / same-rule-different-policy
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1158. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,go.dev -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,go.dev -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1159. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,golang.org -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,golang.org -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,golang.org -> 谷歌服务 (magicrule-google)` (The configured business-category priority applies to this exact conflict.)

### 1160. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1161. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1162. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1163. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1164. semantic-overlap / host-inside-host-suffix
- left: `HOST,redirector.xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,redirector.xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1165. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,go.dev -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,pkg.go.dev -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pkg.go.dev -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1166. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gcpcdn.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1167. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1168. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.offline-maps.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1169. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,gvt1.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.snap.gvt1.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1170. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,redirector.xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,xn--ngstr-lra8j.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.xn--ngstr-lra8j.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1171. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,appspot -> 谷歌服务 (magicrule-google)`
- right: `HOST-SUFFIX,appspot.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,appspot -> 谷歌服务 (magicrule-google)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1172. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,blogspot -> 谷歌服务 (magicrule-google)`
- right: `HOST-KEYWORD,.blogspot -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,blogspot -> 谷歌服务 (magicrule-google)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 1173. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,google -> 谷歌服务 (magicrule-google)` (Both rules are retained. The configured business-category priority provides the first-match order.)

### 1174. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,googlesource -> 谷歌服务 (magicrule-google)`
- right: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST-KEYWORD,googlesource -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1175. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,adservice.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,adservice.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1176. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ai.google.dev -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,ai.google.dev -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1177. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalicore-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alkalicore-pa.clients6.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1178. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1179. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,analytics.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,analytics.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1180. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,android.googlesource.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,android.googlesource.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1181. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1182. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,antigravity.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,antigravity.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1183. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1184. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.clients6.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1185. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,appsgenaiserver-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,appsgenaiserver-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1186. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,avail.googleflights.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,avail.googleflights.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1187. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,c.android.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,c.android.clients.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1188. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cache-management-prod.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cache-management-prod.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1189. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cache.pack.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cache.pack.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1190. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clickserver.googleads.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,clickserver.googleads.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1191. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clients1.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,clients1.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1192. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1193. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cloudaicompanion.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cloudaicompanion.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1194. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1195. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,crashlyticsreports-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,crashlyticsreports-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1196. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,daily-cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,daily-cloudcode-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1197. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1198. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1199. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,dl.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,dl.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1200. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,download.mlcc.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,download.mlcc.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1201. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,download.tensorflow.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,download.tensorflow.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1202. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebase.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebase.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1203. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseappcheck.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseappcheck.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1204. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseappdistribution.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseappdistribution.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1205. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseapptesters.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseapptesters.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1206. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebasedynamiclinks-ipv4.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebasedynamiclinks-ipv4.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1207. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebasedynamiclinks-ipv6.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebasedynamiclinks-ipv6.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1208. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebasedynamiclinks.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebasedynamiclinks.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1209. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseinappmessaging.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseinappmessaging.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1210. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseinstallations.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseinstallations.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1211. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaselogging-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaselogging-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1212. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaselogging.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaselogging.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1213. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseperusertopics-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseperusertopics-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1214. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,firebaseremoteconfig.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,firebaseremoteconfig.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1215. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,fontfiles.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,fontfiles.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1216. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,fonts.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,fonts.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1217. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,geminiweb-pa.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1218. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,geminiweb-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,geminiweb-pa.clients6.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1219. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,google-analytics-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,google-analytics-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1220. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,google-analytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,google-analytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1221. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,google-ohttp-relay-safebrowsing.fastly-edge.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,google-ohttp-relay-safebrowsing.fastly-edge.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1222. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleadservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleadservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1223. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleadservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleadservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1224. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleanalytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleanalytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1225. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleapis-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleapis-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1226. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleapps-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleapps-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1227. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleflights-cn.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleflights-cn.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1228. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleoptimize-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleoptimize-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1229. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googleoptimize.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googleoptimize.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1230. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googlesyndication-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googlesyndication-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1231. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googlesyndication.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googlesyndication.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1232. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletagmanager-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletagmanager-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1233. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletagmanager.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletagmanager.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1234. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletagservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletagservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1235. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletagservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletagservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1236. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1237. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googletraveladservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1238. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,googlevads-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,googlevads-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1239. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,gstaticadssl.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,gstaticadssl.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1240. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,imasdk.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,imasdk.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1241. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,lens.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,lens.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1242. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk-dev.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk-dev.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1243. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk-staging.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk-staging.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1244. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk4.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk4.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1245. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1246. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,notebooklm.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,notebooklm.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1247. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,pagead-googlehosted.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,pagead-googlehosted.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1248. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,performanceparameters.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,performanceparameters.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1249. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,pki-goog.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,pki-goog.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1250. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,pki.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,pki.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1251. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,preprod-publicca.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,preprod-publicca.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1252. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,publicca.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,publicca.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1253. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,qpx.googleflights.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,qpx.googleflights.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1254. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.bigcache.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1255. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.chat.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.chat.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1256. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.mail.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.mail.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1257. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.pack.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.pack.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1258. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,redirector.c.play.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,redirector.c.play.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1259. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing-cache.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing-cache.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1260. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1261. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.ae -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.ae -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1262. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.at -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.at -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1263. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.be -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.be -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1264. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.bg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.bg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1265. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.ca -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.ca -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1266. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.cat -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.cat -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1267. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.ch -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.ch -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1268. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.cl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.cl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1269. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1270. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.cr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.cr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1271. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.id -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.id -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1272. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.il -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.il -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1273. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.in -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.in -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1274. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.jp -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.jp -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1275. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.kr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.kr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1276. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.nz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.nz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1277. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.th -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.th -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1278. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.uk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.uk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1279. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.ve -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.ve -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1280. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.co.za -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.co.za -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1281. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1282. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ar -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ar -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1283. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.au -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.au -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1284. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.bo -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.bo -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1285. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.br -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.br -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1286. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.co -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.co -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1287. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.cu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.cu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1288. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.do -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.do -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1289. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ec -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ec -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1290. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.eg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.eg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1291. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.gt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.gt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1292. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.hk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.hk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1293. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ly -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ly -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1294. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.mx -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.mx -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1295. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.my -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.my -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1296. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ni -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ni -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1297. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.pa -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.pa -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1298. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.pe -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.pe -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1299. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ph -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ph -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1300. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.pk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.pk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1301. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.pr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.pr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1302. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.py -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.py -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1303. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.sg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.sg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1304. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.sv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.sv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1305. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.tr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.tr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1306. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.tw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.tw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1307. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.ua -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.ua -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1308. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.uy -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.uy -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1309. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.com.vn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.com.vn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1310. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.cz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.cz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1311. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.de -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.de -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1312. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.dk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.dk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1313. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.es -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.es -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1314. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.fi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.fi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1315. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.fr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.fr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1316. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.gr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.gr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1317. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.hn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.hn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1318. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.hr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.hr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1319. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.hu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.hu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1320. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.is -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.is -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1321. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.it -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.it -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1322. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.li -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.li -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1323. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.lt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.lt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1324. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.lu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.lu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1325. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.lv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.lv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1326. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.nl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.nl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1327. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.no -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.no -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1328. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.pl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.pl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1329. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.pt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.pt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1330. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.ro -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.ro -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1331. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.ru -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.ru -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1332. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.se -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.se -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1333. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.si -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.si -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1334. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.google.sk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.google.sk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1335. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.googleusercontent.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1336. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,scholar.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,scholar.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1337. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,ssl-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,ssl-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1338. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,tac.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,tac.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1339. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,tools.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,tools.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1340. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,translate.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,translate.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1341. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,update.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,update.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1342. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,wear.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,wear.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1343. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,webchannel-alkalimakersuite-pa.clients6.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1344. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,www-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1345. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www-googletagmanager.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,www-googletagmanager.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1346. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adgoogle.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1347. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adservice.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adservice.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1348. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,adtrafficquality.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,adtrafficquality.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1349. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aicode.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aicode.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1350. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aida.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aida.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1351. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aisandbox-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aisandbox-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1352. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,aistudio.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,aistudio.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1353. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,analytics-alv.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,analytics-alv.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1354. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,antigravity.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,antigravity.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1355. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,avail.googleflights.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1356. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,bard.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,bard.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1357. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blog.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blog.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1358. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,blogger.googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,blogger.googleusercontent.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1359. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,c.android.clients.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,c.android.clients.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1360. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,cache-management-prod.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cache-management-prod.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1361. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,cache.pack.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cache.pack.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1362. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,clickserver.googleads.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1363. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,clientservices.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1364. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,crashlyticsreports-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,crashlyticsreports-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1365. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,deepmind.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,deepmind.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1366. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dg-meta.video.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1367. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,dl.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dl.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1368. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,dl.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dl.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1369. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,download.mlcc.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.mlcc.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1370. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,download.tensorflow.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.tensorflow.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1371. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,fcmatch.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,fcmatch.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1372. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,firebase.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,firebase.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1373. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,flow.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1374. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,flow.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,flow.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1375. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,fontfiles.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,fontfiles.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1376. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,fonts.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,fonts.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1377. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,geller-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,geller-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1378. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1379. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gemini.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gemini.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1380. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativeai.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativeai.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1381. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,generativelanguage.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1382. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ggoogle.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1383. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1384. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-access.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-access.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1385. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1386. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-analytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1387. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google-syndication.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1388. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ad -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ad -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1389. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ae -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ae -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1390. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.al -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.al -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1391. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.am -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.am -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1392. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.as -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.as -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1393. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.at -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.at -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1394. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.az -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.az -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1395. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ba -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ba -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1396. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.be -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.be -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1397. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.berlin -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.berlin -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1398. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bf -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bf -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1399. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1400. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1401. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bj -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bj -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1402. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bs -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bs -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1403. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.bt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.bt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1404. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.by -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.by -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1405. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ca -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ca -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1406. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cat -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cat -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1407. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cd -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cd -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1408. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cf -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cf -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1409. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1410. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ch -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ch -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1411. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ci -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ci -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1412. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1413. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1414. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1415. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1416. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ao -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ao -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1417. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.bw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.bw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1418. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ck -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ck -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1419. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.cr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.cr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1420. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.id -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.id -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1421. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.il -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.il -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1422. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.in -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.in -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1423. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.jp -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.jp -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1424. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ke -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ke -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1425. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.kr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.kr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1426. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ls -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ls -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1427. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ma -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ma -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1428. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.mz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.mz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1429. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.nz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.nz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1430. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.th -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.th -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1431. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.tz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.tz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1432. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ug -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ug -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1433. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1434. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.uz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.uz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1435. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.ve -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.ve -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1436. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.vi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.vi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1437. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.za -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.za -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1438. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1439. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.co.zw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.co.zw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1440. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1441. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.af -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.af -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1442. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ag -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ag -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1443. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ai -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ai -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1444. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ar -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ar -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1445. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.au -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.au -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1446. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bd -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bd -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1447. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bh -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bh -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1448. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1449. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bo -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bo -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1450. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.br -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.br -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1451. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.bz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.bz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1452. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.co -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.co -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1453. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1454. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.cy -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.cy -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1455. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.do -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.do -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1456. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ec -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ec -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1457. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.eg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.eg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1458. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.et -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.et -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1459. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.fj -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.fj -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1460. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gh -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gh -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1461. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1462. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.gt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.gt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1463. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.hk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.hk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1464. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.jm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.jm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1465. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kh -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kh -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1466. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.kw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.kw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1467. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.lb -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.lb -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1468. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ly -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ly -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1469. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1470. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1471. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.mx -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.mx -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1472. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.my -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.my -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1473. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.na -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.na -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1474. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ng -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ng -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1475. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ni -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ni -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1476. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.np -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.np -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1477. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.om -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.om -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1478. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pa -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pa -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1479. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pe -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pe -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1480. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1481. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ph -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ph -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1482. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1483. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.pr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.pr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1484. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.py -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.py -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1485. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.qa -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.qa -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1486. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sa -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sa -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1487. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sb -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sb -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1488. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1489. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1490. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.sv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.sv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1491. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tj -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tj -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1492. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1493. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.tw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.tw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1494. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.ua -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.ua -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1495. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.uy -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.uy -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1496. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vc -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vc -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1497. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.com.vn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.com.vn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1498. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1499. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.cz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.cz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1500. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.de -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.de -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1501. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dev -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dev -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1502. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dj -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dj -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1503. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1504. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1505. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.dz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.dz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1506. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ee -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ee -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1507. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.es -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.es -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1508. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1509. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1510. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.fr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.fr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1511. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ga -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ga -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1512. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ge -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ge -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1513. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1514. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1515. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1516. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1517. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.gy -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.gy -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1518. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1519. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1520. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ht -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ht -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1521. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.hu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.hu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1522. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ie -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ie -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1523. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.im -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.im -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1524. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.iq -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.iq -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1525. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.is -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.is -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1526. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.it -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.it -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1527. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.je -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.je -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1528. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.jo -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.jo -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1529. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1530. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ki -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ki -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1531. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.kz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.kz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1532. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.la -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.la -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1533. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.li -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.li -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1534. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1535. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1536. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1537. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.lv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.lv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1538. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.md -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.md -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1539. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.me -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.me -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1540. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1541. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1542. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ml -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ml -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1543. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1544. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ms -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ms -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1545. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1546. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1547. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.mw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.mw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1548. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ne -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ne -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1549. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1550. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1551. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.no -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.no -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1552. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1553. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.nu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.nu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1554. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.org -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.org -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1555. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1556. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1557. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ps -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ps -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1558. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.pt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.pt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1559. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ro -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ro -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1560. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rs -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rs -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1561. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ru -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ru -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1562. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.rw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.rw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1563. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sc -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sc -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1564. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.se -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.se -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1565. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sh -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sh -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1566. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.si -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.si -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1567. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1568. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1569. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1570. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.so -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.so -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1571. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.sr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.sr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1572. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.st -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.st -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1573. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.td -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.td -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1574. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1575. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1576. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tm -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tm -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1577. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1578. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.to -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.to -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1579. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.tt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.tt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1580. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ventures -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ventures -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1581. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1582. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.vu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.vu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1583. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,google.ws -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,google.ws -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1584. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleacquisitionmigration.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1585. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1586. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadapis.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadapis.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1587. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleads-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleads-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1588. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleads.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleads.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1589. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1590. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1591. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleadsserving.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleadsserving.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1592. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleanalytics.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1593. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1594. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1595. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1596. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1597. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleapps.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleapps.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1598. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlearth.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlearth.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1599. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleblog.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleblog.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1600. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlebot.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlebot.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1601. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecapital.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1602. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecert.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecert.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1603. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecnapps.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1604. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecode.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecode.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1605. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecommerce.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1606. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlecompare.co.uk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1607. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledanmark.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1608. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledomains.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledomains.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1609. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googledrive.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googledrive.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1610. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlee.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlee.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1611. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleearth.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleearth.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1612. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1613. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefiber.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1614. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlefinland.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1615. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleflights-cn.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1616. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemail.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemail.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1617. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemaps.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1618. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlemashups.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1619. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1620. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleoptimize.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1621. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlepagecreator.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1622. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlephotos.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1623. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplay.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplay.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1624. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleplus.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleplus.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1625. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlescholar.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1626. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesource.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesource.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1627. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlestore.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlestore.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1628. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesverige.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1629. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1630. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlesyndication.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1631. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1632. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagmanager.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1633. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1634. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletagservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1635. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1636. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googletraveladservices.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1637. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleusercontent.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1638. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevads-cn.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1639. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googleventures.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googleventures.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1640. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlezip.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlezip.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1641. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,gstaticadssl.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,gstaticadssl.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1642. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,igoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,igoogle.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1643. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,imasdk.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,imasdk.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1644. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,jules.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1645. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,jules.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,jules.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1646. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labs.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1647. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labs.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labs.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1648. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,labstailwind.pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,labstailwind.pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1649. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mail-ads.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mail-ads.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1650. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,makersuite.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,makersuite.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1651. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,marketingplatform.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,marketingplatform.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1652. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mobileads.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mobileads.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1653. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebook.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1654. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebook.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebook.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1655. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1656. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,notebooklm.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1657. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,opal.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1658. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,opal.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,opal.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1659. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,pagead-googlehosted.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pagead-googlehosted.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1660. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,pagead.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pagead.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1661. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,partnerad.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,partnerad.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1662. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,performanceparameters.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,performanceparameters.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1663. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,pki-goog.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,pki-goog.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1664. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,play-fe.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play-fe.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1665. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,play-games.googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play-games.googleusercontent.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1666. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,play-lh.googleusercontent.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play-lh.googleusercontent.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1667. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,play.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1668. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,play.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,play.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1669. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,proactivebackend-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1670. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,qpx.googleflights.net -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1671. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.c.chat.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.c.chat.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1672. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.c.mail.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.c.mail.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1673. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.c.pack.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.c.pack.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1674. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,redirector.c.play.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,redirector.c.play.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1675. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,registry.google -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,registry.google -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1676. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,robinfrontend-pa.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1677. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,safebrowsing-cache.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,safebrowsing-cache.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1678. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,safebrowsing.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1679. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.ae -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.ae -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1680. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.at -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.at -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1681. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.be -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.be -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1682. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.bg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.bg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1683. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.ca -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.ca -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1684. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.cat -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.cat -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1685. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.ch -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.ch -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1686. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.cl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.cl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1687. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1688. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.cr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.cr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1689. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.id -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.id -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1690. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.il -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.il -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1691. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.in -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.in -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1692. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.jp -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.jp -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1693. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.kr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.kr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1694. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.nz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.nz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1695. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.th -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.th -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1696. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.uk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.uk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1697. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.ve -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.ve -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1698. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.co.za -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.co.za -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1699. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1700. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ar -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ar -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1701. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.au -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.au -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1702. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.bo -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.bo -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1703. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.br -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.br -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1704. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.co -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.co -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1705. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.cu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.cu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1706. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.do -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.do -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1707. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ec -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ec -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1708. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.eg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.eg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1709. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.gt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.gt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1710. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.hk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.hk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1711. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ly -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ly -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1712. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.mx -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.mx -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1713. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.my -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.my -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1714. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ni -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ni -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1715. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.pa -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.pa -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1716. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.pe -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.pe -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1717. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ph -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ph -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1718. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.pk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.pk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1719. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.pr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.pr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1720. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.py -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.py -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1721. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.sg -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.sg -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1722. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.sv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.sv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1723. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.tr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.tr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1724. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.tw -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.tw -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1725. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.ua -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.ua -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1726. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.uy -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.uy -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1727. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.com.vn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.com.vn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1728. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.cz -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.cz -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1729. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.de -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.de -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1730. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.dk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.dk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1731. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.es -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.es -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1732. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.fi -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.fi -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1733. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.fr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.fr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1734. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.gr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.gr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1735. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.hn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.hn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1736. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.hr -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.hr -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1737. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.hu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.hu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1738. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.is -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.is -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1739. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.it -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.it -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1740. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.li -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.li -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1741. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.lt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.lt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1742. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.lu -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.lu -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1743. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.lv -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.lv -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1744. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.nl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.nl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1745. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.no -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.no -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1746. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.pl -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.pl -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1747. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.pt -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.pt -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1748. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.ro -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.ro -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1749. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.ru -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.ru -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1750. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.se -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.se -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1751. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.si -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.si -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1752. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.google.sk -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.google.sk -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1753. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,scholar.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,scholar.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1754. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,services.googleapis.cn -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,services.googleapis.cn -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1755. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,ssl-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ssl-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1756. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,stitch.withgoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,stitch.withgoogle.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1757. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tac.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tac.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1758. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thegooglestore.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1759. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,thinkwithgoogle.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1760. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tools.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tools.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1761. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,tools.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tools.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1762. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,update.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,update.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1763. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,wear.googleapis.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,wear.googleapis.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1764. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,withgoogle.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1765. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,www-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,www-google-analytics.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1766. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,www-googletagmanager.l.google.com -> 谷歌服务 (magicrule-google)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,www-googletagmanager.l.google.com -> 谷歌服务 (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1767. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth-pa.clients6.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1768. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,earth.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,earth.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1769. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,kh.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,kh.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1770. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1771. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1772. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1773. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm0.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1774. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1775. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm1.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1776. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1777. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm2.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1778. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1779. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khm3.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1780. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1781. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,khmdb.googleapis.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1782. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (magicrule-google-earth)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mw1.google.com -> 谷歌服务 (magicrule-google-earth)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1783. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,www.googleapis.com -> 谷歌服务 (local-google-drive-1)`
- decision: `ordered-overlap` -> `HOST,www.googleapis.com -> 谷歌服务 (local-google-drive-1)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1784. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,docs.google.com -> 谷歌服务 (local-google-drive-2)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,docs.google.com -> 谷歌服务 (local-google-drive-2)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1785. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,drive.google.com -> 谷歌服务 (local-google-drive-3)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,drive.google.com -> 谷歌服务 (local-google-drive-3)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## microsoft ↔ global-media

### 1786. semantic-overlap / host-inside-host-suffix
- left: `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (local-tvb-tracking)`
- right: `HOST-SUFFIX,azurewebsites.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,tvbtracking.azurewebsites.net -> 国际媒体 (local-tvb-tracking)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1787. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,abcnews.edgesuite.net -> 国际媒体 (magicrule-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1788. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,optimizely.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cdn.optimizely.com -> 国际媒体 (magicrule-global-media-disney)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1789. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,edgesuite.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (magicrule-global-media-hbo)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,hbo.com.edgesuite.net -> 国际媒体 (magicrule-global-media-hbo)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## microsoft ↔ china-direct

### 1790. exact-policy / same-rule-different-policy
- left: `HOST,statics.teams.cdn.office.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST,statics.teams.cdn.office.net -> direct (magicrule-direct)`
- decision: `prefer-category` -> `HOST,statics.teams.cdn.office.net -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 1791. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 1792. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,download.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,download.microsoft.com -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 1793. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,download.visualstudio.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,download.visualstudio.microsoft.com -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 1794. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,download.windowsupdate.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.windowsupdate.com -> direct (magicrule-direct)`
- decision: `prefer-category` -> `HOST-SUFFIX,download.windowsupdate.com -> 全球加速 (magicrule-microsoft)` (The configured business-category priority applies to this exact conflict.)

### 1795. semantic-overlap / host-inside-host-suffix
- left: `HOST,azuremigrate.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azuremigrate.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,azuremigrate.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1796. semantic-overlap / host-inside-host-suffix
- left: `HOST,azuremigratetest.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azuremigratetest.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,azuremigratetest.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1797. semantic-overlap / host-inside-host-suffix
- left: `HOST,azurestackhub.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azurestackhub.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,azurestackhub.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1798. semantic-overlap / host-inside-host-suffix
- left: `HOST,azurestackhubuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azurestackhubuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,azurestackhubuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1799. semantic-overlap / host-inside-host-suffix
- left: `HOST,b.c2r.ts.cdn.office.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,b.c2r.ts.cdn.office.net -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,b.c2r.ts.cdn.office.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1800. semantic-overlap / host-inside-host-suffix
- left: `HOST,cbdstest.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cbdstest.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,cbdstest.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1801. semantic-overlap / host-inside-host-suffix
- left: `HOST,cn.windowssearch.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cn.windowssearch.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,cn.windowssearch.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1802. semantic-overlap / host-inside-host-suffix
- left: `HOST,collaborate.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,collaborate.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,collaborate.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1803. semantic-overlap / host-inside-host-suffix
- left: `HOST,collaborateppe.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,collaborateppe.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,collaborateppe.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1804. semantic-overlap / host-inside-host-suffix
- left: `HOST,ctldl.windowsupdate.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,ctldl.windowsupdate.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,ctldl.windowsupdate.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1805. semantic-overlap / host-inside-host-suffix
- left: `HOST,download.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,download.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1806. semantic-overlap / host-inside-host-suffix
- left: `HOST,download.visualstudio.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,download.visualstudio.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1807. semantic-overlap / host-inside-host-suffix
- left: `HOST,dreamspark.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dreamspark.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,dreamspark.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1808. semantic-overlap / host-inside-host-suffix
- left: `HOST,dreamsparkuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dreamsparkuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,dreamsparkuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1809. semantic-overlap / host-inside-host-suffix
- left: `HOST,f.c2r.ts.cdn.office.net -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,f.c2r.ts.cdn.office.net -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,f.c2r.ts.cdn.office.net -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1810. semantic-overlap / host-inside-host-suffix
- left: `HOST,itacademy.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,itacademy.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,itacademy.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1811. semantic-overlap / host-inside-host-suffix
- left: `HOST,itacademyuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,itacademyuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,itacademyuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1812. semantic-overlap / host-inside-host-suffix
- left: `HOST,lex.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,lex.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,lex.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1813. semantic-overlap / host-inside-host-suffix
- left: `HOST,lexuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,lexuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,lexuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1814. semantic-overlap / host-inside-host-suffix
- left: `HOST,mbs.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mbs.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,mbs.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1815. semantic-overlap / host-inside-host-suffix
- left: `HOST,mpnbenefits.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefits.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,mpnbenefits.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1816. semantic-overlap / host-inside-host-suffix
- left: `HOST,mpnbenefitsrtl.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,mpnbenefitsrtl.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1817. semantic-overlap / host-inside-host-suffix
- left: `HOST,mpnbenefitsrtluat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,mpnbenefitsrtluat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1818. semantic-overlap / host-inside-host-suffix
- left: `HOST,msdn.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdn.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,msdn.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1819. semantic-overlap / host-inside-host-suffix
- left: `HOST,msdprod-ad.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdprod-ad.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,msdprod-ad.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1820. semantic-overlap / host-inside-host-suffix
- left: `HOST,msproduct.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msproduct.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,msproduct.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1821. semantic-overlap / host-inside-host-suffix
- left: `HOST,myvs.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,myvs.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,myvs.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1822. semantic-overlap / host-inside-host-suffix
- left: `HOST,oemsoc.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsoc.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,oemsoc.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1823. semantic-overlap / host-inside-host-suffix
- left: `HOST,oemsocuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsocuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,oemsocuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1824. semantic-overlap / host-inside-host-suffix
- left: `HOST,officecdn.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officecdn.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,officecdn.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1825. semantic-overlap / host-inside-host-suffix
- left: `HOST,officemkt.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemkt.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,officemkt.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1826. semantic-overlap / host-inside-host-suffix
- left: `HOST,officemktuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemktuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,officemktuat.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1827. semantic-overlap / host-inside-host-suffix
- left: `HOST,osrelease.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,osrelease.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,osrelease.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1828. semantic-overlap / host-inside-host-suffix
- left: `HOST,rsm.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,rsm.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,rsm.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1829. semantic-overlap / host-inside-host-suffix
- left: `HOST,sdx.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,sdx.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,sdx.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1830. semantic-overlap / host-inside-host-suffix
- left: `HOST,software.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,software.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,software.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1831. semantic-overlap / host-inside-host-suffix
- left: `HOST,statics.teams.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,statics.teams.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1832. semantic-overlap / host-inside-host-suffix
- left: `HOST,storecorefulfillment.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storecorefulfillment.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,storecorefulfillment.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1833. semantic-overlap / host-inside-host-suffix
- left: `HOST,storeedge.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storeedge.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,storeedge.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1834. semantic-overlap / host-inside-host-suffix
- left: `HOST,surface.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,surface.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1835. semantic-overlap / host-inside-host-suffix
- left: `HOST,surface.downloads.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.downloads.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,surface.downloads.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1836. semantic-overlap / host-inside-host-suffix
- left: `HOST,vlportal.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vlportal.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,vlportal.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1837. semantic-overlap / host-inside-host-suffix
- left: `HOST,volic.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,volic.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,volic.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1838. semantic-overlap / host-inside-host-suffix
- left: `HOST,vscode.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vscode.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,vscode.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1839. semantic-overlap / host-inside-host-suffix
- left: `HOST,vz.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vz.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,vz.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1840. semantic-overlap / host-inside-host-suffix
- left: `HOST,windbg.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,windbg.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST,windbg.download.prss.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1841. semantic-overlap / host-inside-host-suffix
- left: `HOST,res-1.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,res-1.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1842. semantic-overlap / host-inside-host-suffix
- left: `HOST,res-2.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,res-2.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1843. semantic-overlap / host-inside-host-suffix
- left: `HOST,res-h3.public.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,res-h3.public.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1844. semantic-overlap / host-inside-host-suffix
- left: `HOST,res.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST,res.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1845. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azuremigrate.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azuremigrate.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1846. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azuremigratetest.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azuremigratetest.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1847. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azurestackhub.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azurestackhub.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1848. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,azurestackhubuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azurestackhubuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1849. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,b.c2r.ts.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,b.c2r.ts.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1850. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cbdstest.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cbdstest.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1851. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,cn.windowssearch.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,windowssearch.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cn.windowssearch.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1852. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,collaborate.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collaborate.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1853. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,collaborateppe.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collaborateppe.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1854. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,ctldl.windowsupdate.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,windowsupdate.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,ctldl.windowsupdate.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1855. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1856. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,tlu.dl.delivery.mp.microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,tlu.dl.delivery.mp.microsoft.com -> 全球加速 (magicrule-microsoft)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1857. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1858. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1859. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,download.windowsupdate.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,windowsupdate.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.windowsupdate.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1860. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,dreamspark.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dreamspark.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1861. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,dreamsparkuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dreamsparkuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1862. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,f.c2r.ts.cdn.office.net -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,office.net -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,f.c2r.ts.cdn.office.net -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1863. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,itacademy.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itacademy.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1864. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,itacademyuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itacademyuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1865. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,lex.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,lex.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1866. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,lexuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,lexuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1867. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,mbs.download.prss.microsoft.com -> direct (magicrule-direct)`
- right: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mbs.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1868. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefits.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefits.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1869. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1870. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1871. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdn.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msdn.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1872. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdprod-ad.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msdprod-ad.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1873. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msproduct.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msproduct.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1874. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,myvs.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,myvs.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1875. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsoc.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oemsoc.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1876. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsocuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oemsocuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1877. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officecdn.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officecdn.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1878. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemkt.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officemkt.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1879. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemktuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officemktuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1880. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,osrelease.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,osrelease.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1881. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,rsm.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,rsm.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1882. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,sdx.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,sdx.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1883. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,software.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,software.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1884. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storecorefulfillment.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,storecorefulfillment.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1885. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storeedge.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,storeedge.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1886. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,surface.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1887. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.downloads.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,surface.downloads.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1888. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vlportal.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vlportal.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1889. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,volic.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,volic.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1890. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vscode.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vscode.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1891. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vz.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vz.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1892. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,microsoft.com -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,windbg.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,windbg.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1893. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azuremigrate.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azuremigrate.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1894. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azuremigratetest.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azuremigratetest.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1895. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azurestackhub.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azurestackhub.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1896. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,azurestackhubuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,azurestackhubuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1897. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,cbdstest.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,cbdstest.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1898. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,collaborate.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collaborate.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1899. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,collaborateppe.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,collaborateppe.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1900. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dl.delivery.mp.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1901. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1902. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,download.visualstudio.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1903. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dreamspark.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dreamspark.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1904. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,dreamsparkuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,dreamsparkuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1905. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,itacademy.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itacademy.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1906. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,itacademyuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,itacademyuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1907. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,lex.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,lex.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1908. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,lexuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,lexuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1909. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mbs.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mbs.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1910. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefits.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefits.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1911. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefitsrtl.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1912. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,mpnbenefitsrtluat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1913. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdn.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msdn.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1914. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msdprod-ad.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msdprod-ad.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1915. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,msproduct.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,msproduct.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1916. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,myvs.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,myvs.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1917. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsoc.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oemsoc.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1918. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,oemsocuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,oemsocuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1919. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officecdn.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officecdn.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1920. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemkt.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officemkt.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1921. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,officemktuat.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,officemktuat.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1922. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,osrelease.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,osrelease.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1923. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,rsm.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,rsm.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1924. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,sdx.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,sdx.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1925. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,software.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,software.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1926. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storecorefulfillment.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,storecorefulfillment.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1927. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,storeedge.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,storeedge.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1928. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,surface.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1929. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,surface.downloads.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,surface.downloads.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1930. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vlportal.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vlportal.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1931. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,volic.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,volic.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1932. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vscode.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vscode.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1933. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,vz.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,vz.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1934. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,microsoft -> 全球加速 (magicrule-microsoft)`
- right: `HOST-SUFFIX,windbg.download.prss.microsoft.com -> direct (magicrule-direct)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,windbg.download.prss.microsoft.com -> direct (magicrule-direct)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-media ↔ global-media

### 1935. exact-policy / same-rule-different-policy
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `prefer-category` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1936. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,api.mgtv.com -> 国际媒体 (magicrule-global-media-asian)`
- decision: `prefer-category` -> `HOST-SUFFIX,api.mgtv.com -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

## china-media ↔ china-streaming

### 1937. exact-policy / same-rule-different-policy
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST,upos-hz-mirrorakam.akamaized.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (The configured business-category priority applies to this exact conflict.)

### 1938. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1939. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1940. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,api.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1941. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1942. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1943. semantic-overlap / host-inside-host-suffix
- left: `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,app.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1944. semantic-overlap / host-inside-host-suffix
- left: `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,grpc.biliapi.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1945. semantic-overlap / host-inside-host-suffix
- left: `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,m.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1946. semantic-overlap / host-inside-host-suffix
- left: `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,upos-hz-mirrorakam.akamaized.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,upos-hz-mirrorakam.akamaized.net -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1947. semantic-overlap / host-inside-host-suffix
- left: `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,bilibili.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,www.bilibili.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1948. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1949. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 港台番剧 (rulego-china-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## global-media ↔ china-streaming

### 1950. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliintl.com -> direct (magicrule-china-streaming-bilibili)`
- decision: `prefer-category` -> `HOST-SUFFIX,biliintl.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1951. exact-policy / same-rule-different-policy
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,intl-rcd.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1952. exact-policy / same-rule-different-policy
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,intl-subscription.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1953. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (The configured business-category priority applies to this exact conflict.)

### 1954. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (The configured business-category priority applies to this exact conflict.)

### 1955. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iq.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `HOST-SUFFIX,iq.com -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1956. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.44.56.0/22 -> 国际媒体 (magicrule-global-media-asian)`
- right: `IP-CIDR,103.44.56.0/22 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.44.56.0/22 -> 国际媒体 (magicrule-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1957. exact-policy / same-rule-different-policy
- left: `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,103.5.34.153/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,103.5.34.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1958. exact-policy / same-rule-different-policy
- left: `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,104.109.129.153/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,104.109.129.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1959. exact-policy / same-rule-different-policy
- left: `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,110.238.107.47/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,110.238.107.47/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1960. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.120.0/24 -> 国际媒体 (magicrule-global-media-asian)`
- right: `IP-CIDR,118.26.120.0/24 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.120.0/24 -> 国际媒体 (magicrule-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1961. exact-policy / same-rule-different-policy
- left: `IP-CIDR,118.26.32.0/23 -> 国际媒体 (magicrule-global-media-asian)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,118.26.32.0/23 -> 国际媒体 (magicrule-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1962. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.169/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.169/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1963. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.211.4.193/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.211.4.193/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1964. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.131/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1965. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.139/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1966. exact-policy / same-rule-different-policy
- left: `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,203.74.95.153/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,203.74.95.153/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1967. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.11/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.11/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1968. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.201.32.8/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.201.32.8/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1969. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.200/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.200/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1970. exact-policy / same-rule-different-policy
- left: `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,210.71.227.202/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,210.71.227.202/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1971. exact-policy / same-rule-different-policy
- left: `IP-CIDR,223.119.62.225/28 -> 国际媒体 (magicrule-global-media-asian)`
- right: `IP-CIDR,223.119.62.225/28 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,223.119.62.225/28 -> 国际媒体 (magicrule-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1972. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.211.15.99/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1973. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.241.251/32 -> 国际媒体 (magicrule-global-media-asian)`
- right: `IP-CIDR,23.40.241.251/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.241.251/32 -> 国际媒体 (magicrule-global-media-asian)` (The configured business-category priority applies to this exact conflict.)

### 1974. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.40.242.10/32 -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.40.242.10/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.40.242.10/32 -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (The configured business-category priority applies to this exact conflict.)

### 1975. exact-policy / same-rule-different-policy
- left: `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,23.53.32.88/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `prefer-category` -> `IP-CIDR,23.53.32.88/32 -> 国际媒体 (rulego-global-media)` (The configured business-category priority applies to this exact conflict.)

### 1976. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,bilibili.tv -> direct (magicrule-china-streaming-bilibili)`
- right: `HOST-SUFFIX,bilibili.tv -> 国际媒体 (local-global-media-bilibili-intl-1)`
- decision: `prefer-category` -> `HOST-SUFFIX,bilibili.tv -> 国际媒体 (local-global-media-bilibili-intl-1)` (The configured business-category priority applies to this exact conflict.)

### 1977. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache.video.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1978. semantic-overlap / host-inside-host-suffix
- left: `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,biliapi.net -> direct (magicrule-china-streaming-bilibili)`
- decision: `ordered-overlap` -> `HOST,apm-misaka.biliapi.net -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1979. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1980. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1981. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1982. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1983. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1984. semantic-overlap / host-inside-host-suffix
- left: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1985. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1986. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1987. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,inter.ptqy.gitv.tv -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1988. semantic-overlap / host-inside-host-suffix
- left: `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1989. semantic-overlap / host-inside-host-suffix
- left: `HOST,cache-video.iq.com -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,iq.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,cache-video.iq.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1990. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1991. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1992. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,inter.ptqy.gitv.tv -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1993. semantic-overlap / host-inside-host-suffix
- left: `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)`
- right: `HOST-SUFFIX,gitv.tv -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.ptqy.gitv.tv -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1994. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1995. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1996. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1997. semantic-overlap / nested-host-suffix
- left: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `HOST-SUFFIX,iqiyi.com -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1998. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 1999. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-rcd.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2000. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,intl-subscription.iqiyi.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2001. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,cache.video.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST,cache.video.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2002. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,inter.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2003. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-rcd.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2004. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl-subscription.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2005. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,intl.iqiyi.com -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2006. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,akmcdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2007. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,qiyi -> direct (magicrule-china-streaming-iqiyi)`
- right: `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)`
- decision: `ordered-overlap` -> `HOST,chuangcachecdnoversea-tw.inter.iqiyi.com -> 国际媒体 (magicrule-global-media-asian)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2008. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.178/32 -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2009. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,118.26.32.162/32 -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `IP-CIDR,118.26.32.0/23 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,118.26.32.162/32 -> 国际媒体 (magicrule-global-media-iqiyi-intl)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2010. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,203.74.95.130/28 -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `IP-CIDR,203.74.95.131/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,203.74.95.131/32 -> direct (magicrule-china-streaming-iqiyi)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2011. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,203.74.95.130/28 -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `IP-CIDR,203.74.95.139/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,203.74.95.139/32 -> direct (magicrule-china-streaming-iqiyi)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2012. semantic-overlap / ip-cidr-overlap
- left: `IP-CIDR,23.211.15.0/24 -> 国际媒体 (magicrule-global-media-iqiyi-intl)`
- right: `IP-CIDR,23.211.15.99/32 -> direct (magicrule-china-streaming-iqiyi)`
- decision: `ordered-overlap` -> `IP-CIDR,23.211.15.99/32 -> direct (magicrule-china-streaming-iqiyi)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## global-media ↔ proxy

### 2013. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,abc.com -> 国际媒体 (magicrule-global-media-disney)`
- right: `HOST-SUFFIX,abc.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,abc.com -> 国际媒体 (magicrule-global-media-disney)` (The configured business-category priority applies to this exact conflict.)

### 2014. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,naver.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST-SUFFIX,naver.com -> 国际媒体 (rulego-global-media)` (An explicit value-category override applies to this exact conflict.)

### 2015. exact-policy / same-rule-different-policy
- left: `HOST-SUFFIX,now.com -> 国际媒体 (magicrule-global-media-hbo)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-category` -> `HOST-SUFFIX,now.com -> 国际媒体 (magicrule-global-media-hbo)` (The configured business-category priority applies to this exact conflict.)

### 2016. exact-policy / same-rule-different-policy
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (rulego-global-media)`
- right: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- decision: `prefer-value-category` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (An explicit value-category override applies to this exact conflict.)

### 2017. semantic-overlap / host-inside-host-suffix
- left: `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,s3-ap-southeast-1.amazonaws.com -> 国际媒体 (magicrule-global-media-hbo)`
- decision: `ordered-overlap` -> `HOST,s3-ap-southeast-1.amazonaws.com -> 全球加速 (rulego-proxy)` (Both rules are retained. An explicit value-category override provides the first-match order.)

### 2018. semantic-overlap / host-inside-host-suffix
- left: `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)`
- right: `HOST-SUFFIX,now.com -> 全球加速 (rulego-proxy)`
- decision: `ordered-overlap` -> `HOST,api.viu.now.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2019. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST-SUFFIX,googlevideo.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2020. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)`
- decision: `ordered-overlap` -> `HOST,youtubei.googleapis.com -> 国际媒体 (rulego-global-media)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-services ↔ proxy

### 2021. semantic-overlap / host-inside-host-suffix
- left: `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,login.alibaba.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2022. semantic-overlap / host-inside-host-suffix
- left: `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,alibaba.com -> direct (magicrule-china-services-alibaba)`
- decision: `ordered-overlap` -> `HOST,merchant-rating.alibaba.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2023. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,c.mi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2024. semantic-overlap / host-inside-host-suffix
- left: `HOST,c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2025. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,c.mi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2026. semantic-overlap / host-inside-host-suffix
- left: `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)`
- right: `HOST-SUFFIX,mi.com -> direct (magicrule-china-services-xiaomi)`
- decision: `ordered-overlap` -> `HOST,new.c.mi.com -> 全球加速 (rulego-proxy)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## china-direct ↔ proxy

### 2027. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt1-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt1-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2028. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt2-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt2-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2029. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt3-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt3-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2030. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt4-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt4-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2031. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt5-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt5-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2032. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt6-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt6-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2033. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt7-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt7-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2034. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,alt8-mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,alt8-mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

### 2035. semantic-overlap / host-keyword-overlap
- left: `HOST-KEYWORD,google -> 全球加速 (rulego-proxy)`
- right: `HOST,mtalk.google.com -> direct (magicrule-google)`
- decision: `ordered-overlap` -> `HOST,mtalk.google.com -> direct (magicrule-google)` (Both rules are retained. A more specific rule must be evaluated before its broader overlap.)

## Shared infrastructure audit

| Category | Rule | Risk | Reason | Source |
| --- | --- | --- | --- | --- |
| `ai` | `HOST-SUFFIX,algolia.net` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,auth0.com` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,identrust.com` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,intercom.io` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,intercomcdn.com` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,launchdarkly.com` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,segment.io` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,sentry.io` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,statsigapi.net` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `ai` | `HOST-SUFFIX,stripe.com` | `high` | `shared-infrastructure-root` | `magicrule-openai` |
| `apple` | `HOST-SUFFIX,digicert.com` | `high` | `shared-infrastructure-root` | `magicrule-apple` |
| `netflix` | `HOST-SUFFIX,us-west-2.amazonaws.com` | `high` | `shared-infrastructure-root` | `magicrule-netflix` |
| `microsoft` | `HOST-SUFFIX,azure.com` | `medium` | `shared-infrastructure-root` | `magicrule-microsoft` |
| `microsoft` | `HOST-SUFFIX,azureedge.net` | `medium` | `shared-infrastructure-root` | `magicrule-microsoft` |
| `microsoft` | `HOST-SUFFIX,azurefd.net` | `medium` | `shared-infrastructure-root` | `magicrule-microsoft` |
