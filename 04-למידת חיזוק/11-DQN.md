<!-- editorlm-hebrew-html-start -->
<style>
html, body, .vscode-body, .markdown-body, .markdown-preview, #write {
  direction: rtl !important; text-align: right !important;
}
ul, ol { padding-right: 2em !important; padding-left: 0 !important; }
blockquote { border-right: 3px solid #999; border-left: 0; padding-right: 1rem; padding-left: 0; }
@media print {
  html, body, .vscode-body, .markdown-body, .markdown-preview, #write {
    direction: rtl !important; text-align: right !important;
  }
}
</style>
<!-- editorlm-hebrew-html-end -->
<style>
.book { max-width: 900px; margin: auto; line-height: 1.8; font-family: Arial, sans-serif; }
.book .cover { min-height: 680px; box-sizing: border-box; padding: 64px 48px; margin: 24px 0 60px; background: #112b41; color: #f5f8fc; border-top: 9px solid #39c4b5; position: relative; }
.book .cover .eyebrow { color: #81e0d5; font-size: 15px; letter-spacing: 2px; }
.book .cover h1 { color: #fff; font-size: 48px; line-height: 1.3; border: 0; margin: 50px 0 18px; }
.book .cover .subtitle { font-size: 28px; color: #d8e6f0; }
.book .cover .author { font-size: 30px; color: #fff; margin-top: 52px; }
.book .cover .audience { color: #c1d3df; margin-top: 12px; }
.book .cover .motif { direction: ltr; text-align: left; font-family: Consolas, monospace; color: #81e0d5; font-size: 19px; margin-top: 54px; }
.book h1, .book h2, .book h3 { line-height: 1.4; font-weight: 700; }
.book > h1 { font-size: 32px !important; text-align: center !important; margin: 28px 0; }
.book h2 { font-size: 34px !important; text-align: center !important; color: #153b56 !important; background: #eef5fc; border: 0; border-bottom: 4px solid #299c91; border-radius: 10px 10px 0 0; padding: 28px 20px; margin: 24px 0 36px; }
.book h3 { font-size: 24px !important; text-align: right !important; color: #174e49 !important; background: #edf7f5; border: 0; border-right: 5px solid #299c91; border-radius: 6px; padding: 10px 16px; margin: 36px 0 18px; }
.book .chapter { height: 0; margin: 76px 0 0; border-top: 1px solid #ccd7df; break-before: page; page-break-before: always; break-after: avoid; page-break-after: avoid; }
.book .toc { padding: 24px; border-right: 5px solid #39a99d; background: rgba(70,150,155,.09); margin: 24px 0 48px; }
.book pre, .book pre code { direction: ltr !important; text-align: left !important; unicode-bidi: isolate; }
.book pre { box-sizing: border-box !important; width: 100% !important; max-width: 100% !important; margin: 0 !important; padding: 16px 20px; border: 1px solid #ccd7df; border-radius: 8px; line-height: 1.6; overflow-x: auto; }
.book code { direction: ltr; unicode-bidi: isolate; font-family: Consolas, "Courier New", monospace; }
.book pre { background: #f3f6fa !important; color: #1f2937 !important; }
.book pre code, .book pre code.hljs { background: transparent !important; color: #1f2937 !important; }
.book pre .hljs-keyword, .book pre .hljs-literal { color: #6f299c !important; }
.book pre .hljs-string { color: #216338 !important; }
.book pre .hljs-number { color: #075e68 !important; }
.book pre .hljs-comment { color: #526174 !important; }
.book pre .hljs-built_in, .book pre .hljs-title { color: #135b96 !important; }
.book table { width: 75%; max-width: 75%; margin: 18px auto; background: #f3f6fa; }
.book th, .book td { border: 1px solid #ccd7df; padding: 8px 12px; }
.book th, .book td { text-align: right; }
.book .small { font-size: .9em; opacity: .8; }
.book .python-intro { display: flex; align-items: center; gap: 28px; padding: 22px 28px; margin: 24px 0; background: #eef5fc; color: #183e63; border-right: 6px solid #3776ab; border-radius: 10px; }
.book .python-intro strong { font-size: 30px; }
.book .python-fact { background: #fff7d6; color: #423611; border-right: 6px solid #ffd343; border-radius: 8px; padding: 18px 24px; margin: 22px 0; }
.book .python-fact strong { font-size: 24px; }
.book img { max-width: 100%; height: auto; }
.book figure { box-sizing: border-box; width: 75%; max-width: 75%; margin: 24px auto; padding: 16px 20px; background: #f3f6fa; border: 1px solid #ccd7df; border-radius: 8px; text-align: center; }
.book figure img { display: block; margin: auto; }
.book figcaption { direction: rtl; text-align: center; font-size: .9em; color: #445566; }
@media print { .book > h2 { break-before: page; page-break-before: always; } }
.book .screen-strip { width: 760px; max-width: 100%; height: 220px; overflow: hidden; border: 1px solid #bccad5; border-radius: 8px; margin: 20px auto 8px; direction: ltr; }
.book .screen-strip.output { height: 265px; }
.book .screen-strip img { display: block; width: 1745px; max-width: none; }
.book .screen-menu { width: 400px; max-width: 100%; height: 295px; overflow: hidden; direction: ltr; margin: 20px auto 8px; border: 1px solid #bccad5; border-radius: 8px; }
.book .screen-menu img { display: block; width: 1745px; max-width: none; }
.book .code-panel { box-sizing: border-box !important; display: block !important; width: 75% !important; max-width: 75% !important; margin: 18px auto !important; }
@media print {
  .book .cover { min-height: 85vh; break-after: page; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .book pre { white-space: pre-wrap; break-inside: avoid; }
  .book .chapter { margin: 0; border: 0; }
  .book h1, .book h2, .book h3 { break-after: avoid; page-break-after: avoid; break-inside: avoid; }
  .book h2 { margin-top: 0; }
  .book h2, .book h3 { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
}
</style>

<style>
.book .book-nav { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; align-items: center; padding: 16px 0; margin: 20px 0 32px; border-top: 1px solid #ccd7df; border-bottom: 1px solid #ccd7df; }
.book .book-nav a { display: inline-block; padding: 10px 18px; border-radius: 8px; background: #eef5fc; color: #153b56 !important; border: 1px solid #b5ccd9; text-decoration: none !important; font-size: 16px; font-weight: bold; }
.book .book-nav a.toc-link { background: #174e49; color: #fff !important; border-color: #174e49; }
.book .book-nav a:hover, .book .book-nav a:focus { background: #d4eee8; color: #153b56 !important; outline: 2px solid #299c91; outline-offset: 2px; }
.book .section-list { line-height: 2; }
@media print { .book .book-nav { display: none; } }

/* Explicit Hebrew direction, including prose beginning with English. */
.book p, .book ul, .book ol, .book li,
.book blockquote, .book h1, .book h2, .book h3,
.book h4, .book th, .book td {
  direction: rtl !important;
  text-align: right !important;
  unicode-bidi: isolate;
}
/* Chapter titles keep their agreed centered layout. */
.book h2 { text-align: center !important; }
.book pre, .book pre code, .book .code-panel {
  direction: ltr !important;
  text-align: left !important;
  unicode-bidi: isolate;
}
</style>

<style>
/* Display math renders left-to-right and centered, independent of the RTL page. */
.book .math-panel, .book .math-panel .katex-display, .book .math-panel .katex {
  direction: ltr !important;
  text-align: center !important;
  unicode-bidi: isolate;
}
.book .math-panel { box-sizing: border-box; width: 75%; max-width: 75%; margin: 20px auto; padding: 16px 20px; background: #f3f6fa; color: #1f2937; border: 1px solid #ccd7df; border-radius: 8px; overflow-x: auto; font-size: 1.1em; }
.book .math-panel .katex-display { margin: 0; }
.book .math-panel p { margin: 0; }
.book .grid-panel { box-sizing:border-box; width:75%; max-width:75%; margin:20px auto; padding:16px 20px; background:#f3f6fa; border:1px solid #ccd7df; border-radius:8px; }
.book .grid { direction:ltr!important; width:auto!important; max-width:100%!important; margin:0 auto; border-collapse:collapse; background:#fff; }
.book .grid td { direction:ltr!important; text-align:center!important; width:64px; height:48px; border:1px solid #8199aa; }
.book .grid .goal { background:#d3efdc; } .book .grid .bad { background:#f4d7d7; }
</style>

<div class="book" dir="rtl" lang="he">

<nav class="book-nav" aria-label="ניווט בספר">
<a href="10-TD%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="12-DQN%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">הבא ←</a>
</nav>

## ד.11 — למידת חיזוק עמוקה

**המצגת:** [DQN](../../../sources/RL/6.DQN.pptx) · **קוד:** [DQN_Trainer.py במאגר Tic_Tac_Toe_DQN](https://github.com/MarkmanGilad/Tic_Tac_Toe_DQN/blob/main/DQN_Trainer.py) · [המאמן בגרסת הספר](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_train.py) · [כל קובצי הקוד בגיטהב](https://github.com/MarkmanGilad/book/tree/main/assets/rl/code)

עד עכשיו כל הסוכנים שבנינו שמרו את מה שלמדו בטבלה: לכל מצב, או לכל זוג מצב ופעולה, תא משלו ובתא מספר. באיקס עיגול זה עבד יפה, כי מספר הלוחות האפשריים קטן, ואפילו טבלת AfterState מהפרק הקודם הסתפקה באלפי רשומות. אבל נסו לדמיין את אותה טבלה למשחק שחמט, או למכונית אוטונומית שמצבה מתואר במהירויות ובמרחקים רציפים. שם אין טבלה שתספיק, ורוב המצבים לעולם לא ייפגשו פעמיים.

**למידת חיזוק עמוקה** פותרת את הבעיה בכך שהיא מחליפה את הטבלה ברשת נוירונים. במקום לשמור כל ערך בתא נפרד, הרשת מחשבת אותו. כאן נפגשים שני חלקי הספר: בחלק ג למדנו שרשת נוירונים היא פונקציה עם משקלים, שמאמנים אותה להתאים קלט לפלט ושהיא יודעת להכליל לקלטים שלא ראתה. בחלק ד למדנו איך לבנות יעד למידה מתגמול ומהערכת ההמשך. **Deep Q-Network — DQN** מחבר את השניים.

נבנה את האלגוריתם בשלושה שלבים, בדיוק בסדר שבו הוא נבנה במקור. תחילה נחליף את טבלת Q ברשת נוירונים, ולא נשנה דבר נוסף. אחר כך נוסיף מאגר של מעברים, **Replay Buffer**, שממנו דוגמים את הדוגמאות לאימון. ולבסוף נוסיף רשת שנייה, **רשת המטרה**, שמחשבת את יעדי האימון. כל שלב פותר בעיה שהשלב הקודם חשף.

### החיסרון בטבלאות ערכים

כל הפתרונות שראינו עד כה, מ־Policy Iteration ועד Q-learning, נשענו על מבנה נתונים שהחזיק את הערכים: טבלת V או טבלת Q, ובה רשומה לכל מצב, או לכל זוג מצב ופעולה, בסביבה. במקרים רבים מספר המצבים האפשריים גדול כל כך שאין אפשרות מעשית לשמור את כולם בזיכרון המחשב, ולעיתים הוא אין־סופי:

| המשחק או הסביבה | מספר המצבים |
| --- | --- |
| דמקה | 10<sup>20</sup> |
| שחמט | כ־10<sup>40</sup> |
| Go | 10<sup>170</sup> |
| רכב אוטונומי | אין־סופי |

ויש קושי שני, גם אם היה מקום לכולם: הזמן הדרוש כדי לעדכן מיליארדי רשומות, שוב ושוב עד להתכנסות, עצום ואינו מעשי. בשני המקרים הבעיה אינה בקוד שכתבנו אלא במבנה הנתונים עצמו.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L5-L7] -->

### הפתרון — רשת נוירונים במקום טבלה

טבלת ערכים היא למעשה פונקציה: מכניסים מצב ומקבלים מספר, V(s), או מכניסים מצב ופעולה ומקבלים מספר, Q(s,a). באלגוריתמים שלמדנו עדכנו את ערכי הטבלה בכל פעם "בכיוון הטעות", למשל בעדכון TD של [פרק ד.9](09-Temporal%20Difference.md):

<div class="math-panel" dir="ltr">

$$
V(s) \leftarrow V(s) + \alpha \left[ R + \gamma V(s') - V(s) \right]
$$

</div>

התחלנו מערכים אקראיים וביצענו עדכונים חוזרים ונשנים, עד שהערכים התייצבו והטעות נעשתה קטנה. זה דומה מאוד לאימון רשת נוירונים: גם שם מתחילים ממשקלים אקראיים, ובאמצעות עדכונים חוזרים מזיזים את המשקלים לכיוון המינימום של הטעות. ההבדל הוא שברשת אין תא לכל מצב. יש קבוצה אחת של משקלים, שמשמשת לחישוב הערך של כל מצב. לכן רשת יכולה לייצג פונקציית ערך גם על מרחב מצבים ענק, ואפילו רציף, בלי לשמור רשומה לכל מצב.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L9-L11] -->

### רשת נוירונים בלמידת חיזוק

באימון רשת בלמידה מפוקחת עבדנו לפי תבנית קבועה, שנשארת כאן כמות שהיא:

1. מקבלים זוגות של נתונים: קלט X ותוצאה Y, שהיא המטרה.
2. מבצעים חלחול קדימה ומחשבים את התוצאה המשוערת <span dir="ltr">ŷ = Model(X)</span>.
3. מחשבים את הטעות <span dir="ltr">loss = (ŷ − y)²</span>.
4. מבצעים חלחול לאחור כדי לחשב את הנגזרות של פונקציית הטעות.
5. מעדכנים את הפרמטרים של הרשת לפי הטעות, באלגוריתם SGD.

בלמידת חיזוק נשתמש באותו אלגוריתם, ונחליף את הטבלה V ברשת נוירונים. נסמן את פלט הרשת ב־V̂(s;w), כאשר w הם משקלי הרשת, והסימון ;w מזכיר שהערך אינו נשלף מטבלה אלא מחושב, ושהוא תלוי במשקלים הנוכחיים. נוסחת העדכון נראית כמעט אותו דבר, אלא שכל הערכים מגיעים עכשיו מהרשת:

<div class="math-panel" dir="ltr">

$$
\hat{V}(s;w) \leftarrow \hat{V}(s;w) + \alpha \left[ \textcolor{#c00000}{R + \gamma \hat{V}(s';w)} - \hat{V}(s;w) \right]
$$

</div>

הביטוי באדום הוא בדיוק המטרה שחסרה לנו כדי למלא את התבנית של הלמידה המפוקחת. את שלושת הרכיבים של התבנית, קלט, תחזית ומטרה, אפשר עכשיו למלא גם לפונקציית V וגם לפונקציית Q:

| | פונקציית V | פונקציית Q |
| --- | --- | --- |
| הקלט X | S | <span dir="ltr">(S, A)</span> |
| התוצאה המשוערת ŷ | <span dir="ltr">V̂(S;w)</span> | <span dir="ltr">Q̂(S,A;w)</span> |
| המטרה y | <span dir="ltr">R + γ·V̂(S′;w)</span> | <span dir="ltr">R + γ·Q̂(S′,A′;w)</span> |

ההבדל היחיד מלמידה מפוקחת הוא **מקור המטרה**. אין לנו מראש תווית שאומרת מהו הערך הנכון של כל מצב; את המטרה בונים מהתגמול שהתקבל ומהערכת ההמשך, בדיוק כמו בעדכון TD. הסוכן מייצר לעצמו את ה"תוויות" תוך כדי משחק.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L13-L15] -->

### סוגי רשתות נוירונים

נשתמש באלגוריתם Q-learning ונחליף את טבלת Q ברשת נוירונים, שהיא פונקציה. במקום לעדכן ערכים של V או Q בטבלה, נעדכן את הפרמטרים של הרשת. לפני כן צריך להחליט מה בדיוק הרשת מקבלת ומה היא מחזירה, ויש לכך שלוש צורות:

| קלט | פלט | שימוש |
| --- | --- | --- |
| מצב, או AfterState | ערך יחיד <span dir="ltr">v̂(s;w)</span> | קירוב פונקציית הערך של המצב |
| מצב ופעולה | ערך Q יחיד <span dir="ltr">q̂(s,a;w)</span> | מחשבים ציון לכל פעולה מועמדת |
| מצב בלבד | ערך Q לכל פעולה, <span dir="ltr">q̂(s,a₁;w) … q̂(s,aₘ;w)</span> | כל הפעולות במעבר יחיד |

<figure>
<img src="../assets/slides/1a860b9f9f/image8.png" alt="שלוש רשתות: קלט s ופלט v; קלט s ו־a ופלט q יחיד; קלט s ופלט q לכל פעולה" style="width:100%;max-width:100%;height:auto;">
<figcaption>שלוש הצורות מהטבלה, משמאל לימין: רשת שמקבלת מצב ומחזירה ערך אחד v̂(s,w); רשת שמקבלת מצב ופעולה ומחזירה ערך Q יחיד q̂(s,a,w); ורשת שמקבלת מצב בלבד ומחזירה ערך לכל אחת מהפעולות. w הם המשקלים הנלמדים, והקו הגלי בתוך כל תיבה מזכיר שהרשת היא פונקציה.</figcaption>
</figure>

הצורה השלישית היא הנפוצה בספרות: הרשת מחזירה ערך לכל פעולה במעבר יחיד. בהדגמה באיקס עיגול, בפרק הבא, נבחר דווקא בצורה השנייה: מצב ופעולה בקלט ומספר אחד בפלט. בכל מצב נריץ את הרשת על כל הפעולות החוקיות ונבחר את זו שקיבלה את הערך הגבוה ביותר. הבחירה הזאת נוחה במשחק שבו קבוצת הפעולות החוקיות משתנה ממצב למצב, כי מעריכים רק פעולות חוקיות.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L17-L21] -->

### האלגוריתם DQN

האלגוריתם שנלמד פותח בידי צוות חוקרים ב־Google DeepMind ופורסם בשני מאמרים, בשנים 2013 ו־2015. באותם מאמרים הדגימו החוקרים כיצד אפשר ללמד סוכן לשחק משחקי Atari כשהקלט הוא תמונות מסך המשחק בלבד, כמו אצל שחקן אנושי, ואותו סוכן, עם אותה רשת ואותו אלגוריתם, למד עשרות משחקים שונים:

- [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602), V. Mnih ואחרים, NIPS Deep Learning Workshop 2013.
- [Human-level Control Through Deep Reinforcement Learning](https://www.nature.com/articles/nature14236), V. Mnih ואחרים, Nature 2015.

<figure>
<img src="../assets/slides/1a860b9f9f/image4.jpeg" alt="מסך של משחק Breakout מקונסולת Atari 2600: לבנים צבעוניות, מחבט וכדור" style="width:360px;max-width:100%;height:auto;">
<figcaption>משחק Breakout מקונסולת Atari 2600, אחד המשחקים שסוכן DQN למד לשחק מתוך תמונת המסך בלבד.</figcaption>
</figure>

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L23-L27] -->

### נקודת המוצא — Q-learning

נפתח את האלגוריתם בשלבים, מתוך [Q-learning](09-Temporal%20Difference.md#q-learning) עם טבלת Q כפי שלמדנו בפרק ד.9. הפסאודו־קוד שם הוא נקודת המוצא, ובכל שלב נסמן באדום רק את השורות שהשתנו. הפרט מאותו פרק שחשוב במיוחד לכאן: הסוכן בוחר את הפעולה שהוא מבצע בפועל לפי ε-greedy, אבל הפעולה הבאה שנכנסת ליעד נבחרת לפי טבלת Q בלבד, בלי ε, כלומר לפי הערך המרבי <span dir="ltr">max Q(S′,a)</span>. זו התכונה שהופכת את Q-learning ל־off-policy, ובהמשך הפרק נראה למה היא הכרחית לנו.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L29-L31] -->

### שלב ראשון — מחליפים את הטבלה בפונקציה

כזכור, רשת נוירונים היא פונקציה שמקבלת קלט ומחזירה פלט באמצעות פרמטרים w, שאותם מעדכנים תוך כדי האימון. נסמן את פונקציית הרשת שמחליפה את הטבלה:

<div class="math-panel" dir="ltr">

$$
Q(s,a) \approx \hat{Q}(s,a;w)
$$

</div>

חישוב ערך Q הוא למעשה פעולת ה־forward שאנחנו מבצעים ברשת. כל מה שנותר הוא להחליף, בנוסחאות בלמן שלמדנו, את הטבלה בפונקציה של הרשת.

עדכון של רשומה בטבלה שינה רק את הערך שלה. עדכון משקלי הרשת עשוי לשנות את התחזיות לקלטים רבים. זו תכונת ההכללה שראינו בחלק ג, וכאן היא גם היתרון וגם מקור הקושי: הרשת לומדת ש"מצבים שדומים ללוח הזה שווים בערך כך וכך", אבל כל צעד אימון עלול לשנות מעט גם את מה שכבר נלמד על לוחות אחרים. נחזור לנקודה הזאת כשנוסיף את רשת המטרה.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L33-L35] -->

### פונקציית הטעות loss

אחרי ההחלפה מתקבלות שתי נוסחאות עדכון, של הטבלה ושל הרשת, שההבדל היחיד ביניהן הוא מקור הערכים:

<div class="math-panel" dir="ltr">

$$
\begin{gathered}
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ \textcolor{#c00000}{R + \gamma \max_{a'} Q(s',a')} - Q(s,a) \right] \\[6pt]
\hat{Q}(s,a;w) \leftarrow \hat{Q}(s,a;w) + \alpha \left[ \textcolor{#c00000}{R + \gamma \max_{a'} \hat{Q}(s',a';w)} - \hat{Q}(s,a;w) \right]
\end{gathered}
$$

</div>

לביטוי בסוגריים המרובעים קראנו TD error, כי הוא מודד את הטעות בין הערך בטבלה, וכעת בפונקציה, לבין הערך "הנכון יותר" שבנינו מהתגמול ומההמשך. אבל את השורה השנייה אי אפשר לבצע כמות שהיא: לפלט של רשת אין תא שאפשר להציב בו ערך חדש. מה שכן אפשר לעשות הוא להשתמש בטעות הזאת בתוך פונקציית הטעות MSELoss מחלק ג:

<div class="math-panel" dir="ltr">

$$
\text{loss} = \left[ R + \gamma \max_{a'} \hat{Q}(s',a';w) - \hat{Q}(s,a;w) \right]^2
$$

</div>

זו שגיאת TD בריבוע. בטבלה הזזנו את הערך ב־α כפול השגיאה; ברשת, מזעור ה־loss בעזרת ירידה בגרדיאנט מזיז את המשקלים כך שהתחזית תתקרב ליעד. בזמן צעד האימון מתייחסים ליעד כאל מספר קבוע ולא מעבירים דרכו גרדיאנט; הגרדיאנט מחושב רק דרך התחזית Q̂(s,a;w) שאנחנו מנסים לקרב. עבור אצווה של דוגמאות MSELoss מחשבת את ממוצע ריבועי השגיאות. מכאן והלאה, כדי לא להכביד, נכתוב Q(s,a;w) בלי הכובע: הסימון ;w מספיק כדי להזכיר שהערך מחושב ברשת.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L37-L39] -->

### Deep Q-learning — האלגוריתם ההתחלתי

יש לנו רשת, יעד ופונקציית טעות, ואפשר לכתוב את הגרסה הראשונה של האלגוריתם. במילים: מאתחלים את הרשת במשקלים אקראיים. בכל צעד של המשחק בוחרים פעולה בעזרת הרשת ו־ε-greedy, מבצעים אותה ומקבלים תגמול ומצב הבא. מחשבים את התחזית של הרשת לזוג שבוצע, בונים את היעד מהתגמול ומההמשך, מחשבים loss, מפעילים backward ומבצעים צעד של האופטימייזר. ממשיכים כך עד סוף המשחק ומתחילים משחק חדש. לעומת הפסאודו־קוד של Q-learning בפרק ד.9, השורות שהשתנו מסומנות באדום:

<div class="code-panel" dir="ltr">
<pre><code><span style="color:#c00000;font-weight:bold">Initialize network Q(s, a; w) with random weights w</span>
For each episode:
    Initialize S
    Repeat:
        Choose A using <span style="color:#c00000;font-weight:bold">Q(S, a; w)</span> and epsilon-greedy
        Perform A and observe R, S'
        <span style="color:#c00000;font-weight:bold">prediction = Q(S, A; w)                       # forward</span>
        If S' is terminal:
            target = R
        Else:
            target = R + gamma * max Q(S', legal action<span style="color:#c00000;font-weight:bold">; w</span>)
        <span style="color:#c00000;font-weight:bold">loss = (target - prediction)^2                # MSELoss</span>
        <span style="color:#c00000;font-weight:bold">loss.backward()                               # gradients</span>
        <span style="color:#c00000;font-weight:bold">optimizer.step()                              # update w</span>
        S = S'
    Until S is terminal
</code></pre>
</div>

שימו לב מה **לא** השתנה: מבנה הלולאה, בחירת הפעולה ב־ε-greedy, הדגימה מהסביבה וההעברה <span dir="ltr">S = S′</span> נשארו בדיוק כמו בטבלה. השתנתה רק שורת העדכון: במקום השמה לתא, שלוש שורות של צעד אימון מחלק ג. המונח "אפוק" מקבל כאן משמעות של משחק אחד, אפיזודה, ולא של מעבר על כל מערך הנתונים.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L41-L43] -->

### מצב סופי — Terminal State

הערך של מצב סופי הוא תמיד אפס, כי אין אחריו תגמולים עתידיים. בטבלאות V ו־Q דאגנו שערכי המצבים הסופיים יישארו אפס. ברשת נוירונים אי אפשר לקבוע מה יהיה הפלט עבור מצב סופי: הרשת היא פונקציה עם פרמטרים, והיא מחזירה מספר כלשהו, ובוודאי שאחרי עדכון הפרמטרים אין לדעת מה הוא יהיה. לכן בקוד מבצעים חישוב נפרד למצבים סופיים ומסירים במפורש את חלק העתיד:

<div class="math-panel" dir="ltr">

$$
\text{loss} = \begin{cases} \left[ R - Q(S,A;w) \right]^2 & \text{if done} \\[6pt] \left[ R + \gamma \max_{a'} Q(S',a';w) - Q(S,A;w) \right]^2 & \text{otherwise} \end{cases}
$$

</div>

זו בדיוק ההסתעפות שכבר מופיעה בפסאודו־קוד למעלה: במעבר סופי היעד הוא **R בלבד**. למשל, אחרי מהלך מנצח היעד הוא 1, גם אם הרשת מחזירה תחזיות שונות עבור הלוח הסופי. התגמול של המעבר לסיום עדיין נכלל; רק ההמשך מושמט.

הגרסה ההתחלתית הזאת עובדת על הנייר, אבל בפועל האימון בה נוטה להיות לא יציב. בשני השלבים הבאים נזהה שתי סיבות לכך, ולכל אחת נוסיף רכיב שפותר אותה.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L45-L47] -->

<a id="replay"></a>
### Replay Buffer

אחת הבעיות המרכזיות ביישום רשת נוירונים באלגוריתם TD, שמשתמש ב־bootstrapping, היא שהדגימות מהסביבה תלויות זו בזו. בזמן האימון נוצרת שרשרת של מצבים ופעולות שכל אחד מהם נובע מקודמו, ובנוסף כל הדגימות שייכות למשחק מסוים ולמדיניות מסוימת, ואינן אקראיות. בחלק ג, כשאימנו רשת על מערך נתונים, ערבבנו את הדוגמאות וחילקנו אותן לאצוות, כדי שכל אצווה תייצג את המגוון כולו. כדי שלמידת מכונה תצליח, הקלט צריך לקיים את התנאי **i.i.d — Independent and Identically Distributed**: דוגמאות בלתי תלויות ומאותה התפלגות. שרשרת של מעברים עוקבים מאותו משחק רחוקה מכך: אם נעדכן בכל רגע רק לפי המעבר האחרון, האימון יתבסס על מקטע צר של ההתנסות, והרשת עלולה "לשכוח" מה שלמדה ממשחקים קודמים.

הפתרון הוא מבנה נתונים, **Replay Buffer**, ששומר את הדגימות שאנחנו מבצעים מהסביבה. כל רשומה מכילה מעבר אחד: `(state, action, reward, next_state, done)`. עדכון הרשת ייעשה באמצעות אצוות (batches) אקראיות שנדגמות מהמאגר, ולא מיד אחרי קבלת כל דגימה. הדגימה מערבבת חוויות ממשחקים ומרגעים שונים, ומאפשרת ללמוד שוב ושוב ממעבר שכבר נאסף. המאגר מוגבל בגודלו: כשנכנסים מעברים חדשים מעבר לקיבולת, הישנים ביותר יוצאים, וכך נשמרים בו תמיד הנתונים האחרונים, שנדגמו לפי המדיניות המעודכנת יותר.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L49-L53] -->

### Deep Q-learning עם Replay Buffer

נוסיף את המאגר לאלגוריתם. במילים: מאתחלים, נוסף לרשת, מאגר בגודל N. בכל צעד של המשחק בוחרים פעולה ומבצעים אותה כמו קודם, אבל את המעבר שהתקבל שומרים במאגר במקום לאמן עליו ישירות. אחר כך דוגמים מהמאגר אצווה אקראית של מעברים, ומבצעים על כל אחד מהם את צעד האימון מהשלב הקודם. התוספות מסומנות באדום:

<div class="code-panel" dir="ltr">
<pre><code>Initialize network Q(s, a; w) with random weights w
<span style="color:#c00000;font-weight:bold">Initialize replay buffer RB with capacity N</span>
For each episode:
    Initialize S
    Repeat:
        Choose A using Q(S, a; w) and epsilon-greedy
        Perform A and observe R, S'
        <span style="color:#c00000;font-weight:bold">Store (S, A, R, S', done) in RB</span>
        <span style="color:#c00000;font-weight:bold">Sample a random minibatch from RB</span>
        <span style="color:#c00000;font-weight:bold">For each (s, a, r, s', done) in the minibatch:</span>
            prediction = Q(s, a; w)
            If done:
                target = r
            Else:
                target = r + gamma * max Q(s', legal action; w)
            loss = (target - prediction)^2
            loss.backward()
            optimizer.step()
        S = S'
    Until S is terminal
</code></pre>
</div>

בכל צעד של המשחק מתרחשים עכשיו שני דברים נפרדים: איסוף מעבר חדש למאגר, ואימון על אצווה אקראית מהמאגר, שרוב חבריה מגיעים ממשחקים קודמים. לכן חשוב להבחין בין המצב **החי** של המשחק, שסימנו באות גדולה S, לבין המצבים שנדגמו מהמאגר לצורך האימון, באות קטנה s. אחרי האימון ממשיכים את המשחק מן המצב שאליו הגענו עכשיו, <span dir="ltr">S = S′</span>, ולא ממצב ישן שנשלף במקרה מהמאגר. הלולאה "לכל דגימה" כתובה כאן לשם הבהירות; בקוד מעבירים את כל האצווה לרשת בבת אחת, כטנסור אחד, בדיוק כפי שעשינו בחלק ג, ו־MSELoss מחשבת את ממוצע ריבועי השגיאות של האצווה.

כאן נכנס לתמונה היתרון של Q-learning כאלגוריתם off-policy. המעברים במאגר נאספו כשהרשת הייתה במצב אחר, ואולי גם עם ε אחר, ובכל זאת מותר ללמוד מהם, כי היעד משתמש בפעולה הטובה ביותר במצב הבא ולא בפעולה שנבחרה אז בפועל. ב־SARSA, שלומד את המדיניות שבה הוא משחק, מעבר ישן היה מלמד על מדיניות שכבר אינה קיימת.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L55-L57] -->

### יעד שאינו יציב — Non-stationarity of targets

בעיה נוספת נעוצה בכך שבאימון רשת נוירונים ערכי המטרה קבועים ואינם משתנים: השאלה אם תמונה מסוימת היא חתול או לא חתול אינה משתנה במהלך האימון. לעומת זאת, בלמידת חיזוק אנחנו משתמשים ב־bootstrapping, ולכן המטרות שלנו משתנות תוך כדי הלמידה. ערך המטרה <span dir="ltr">R + γ·max Q(S′,a;w)</span> משתנה בכל פעם שאנחנו משנים את פרמטרי הרשת, כי אותה רשת מחשבת גם את התחזית וגם את המטרה. אנחנו מנסים להתקרב למספר שזז בזמן שאנחנו מתאמנים. בטבלה זה היה קל יותר: עדכון תא אחד לא שינה את התאים האחרים. ברשת, צעד אימון על מצב אחד משנה, בגלל ההכללה, גם את התחזית למצב הבא, ואיתה את היעד עצמו. במקרים גרועים הרשת "רודפת אחרי הזנב של עצמה" והערכים מתבדרים.

הפתרון הוא להשתמש בשתי רשתות נוירונים בעלות אותו מבנה אך עם פרמטרים שונים:

- **הרשת הראשית**, בעלת המשקלים w, משמשת לבחירת הצעדים, <span dir="ltr">Q(S,A;w)</span>, ואותה מעדכנים בכל איטרציה.
- **רשת המטרה**, בעלת המשקלים w⁻, משמשת לחישוב המטרות, <span dir="ltr">R + γ·max Q(S′,a;w⁻)</span>. היא קבועה למשך C צעדים ואינה מתעדכנת. אחרי C צעדים מעתיקים אליה את משקלי הרשת הראשית: <span dir="ltr">w⁻ ← w</span>.

כך היעדים אינם משתנים בעקבות כל צעד גרדיאנט, אלא נשארים קבועים לאורך תקופה שלמה של אימון, והרשת הראשית יכולה להתכנס אליהם. אחרי ההעתקה היעדים מתעדכנים בבת אחת לפי כל מה שנלמד בינתיים. רשת המטרה אינה מקור של תשובות אמת, אלא "תמונת מצב" ישנה יותר של אותה רשת.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L59-L61] -->

### Deep Q-learning (DQN) — האלגוריתם המלא

נוסיף את רשת המטרה, וזהו DQN. במילים: מאתחלים את הרשת הראשית, ומעתיקים את משקליה לרשת המטרה. בכל צעד של המשחק בוחרים פעולה בעזרת הרשת **הראשית** ו־ε-greedy, שומרים את המעבר במאגר ודוגמים אצווה. את התחזית מחשבים ברשת הראשית, ואת ערך ההמשך שביעד ברשת **המטרה**. ה־loss מעדכן את הרשת הראשית בלבד. אחת ל־C משחקים מעתיקים את משקלי הראשית למטרה. התוספות לעומת השלב הקודם מסומנות באדום:

<div class="code-panel" dir="ltr">
<pre><code>Initialize main network Q(s, a; w) with random weights w
<span style="color:#c00000;font-weight:bold">Initialize target network Q(s, a; w⁻) and copy: w⁻ ← w</span>
Initialize replay buffer RB with capacity N
For each episode:
    Initialize S
    Repeat:
        Choose A using Q(S, a; w) and epsilon-greedy
        Perform A and observe R, S'
        Store (S, A, R, S', done) in RB
        Sample a random minibatch from RB
        For each (s, a, r, s', done) in the minibatch:
            prediction = Q(s, a; w)
            If done:
                target = r
            Else:
                target = r + gamma * max Q(s', legal action; <span style="color:#c00000;font-weight:bold">w⁻</span>)
            loss = (target - prediction)^2
            loss.backward()
            optimizer.step()
        S = S'
    Until S is terminal
    <span style="color:#c00000;font-weight:bold">Every C episodes: w⁻ ← w</span>
</code></pre>
</div>

השינוי בנוסחת היעד הוא תו אחד, w⁻ במקום w, ומשמעותו שערכי ההמשך מגיעים מרשת המטרה:

<a id="dqn-target"></a>
<div class="math-panel" dir="ltr">

$$
y = \begin{cases} R & \text{if done} \\[6pt] R + \gamma \max_{a' \in A(S')} Q(S',a';w^{-}) & \text{otherwise} \end{cases}
$$

</div>

כמה דגשים למימוש. יחידת הסנכרון כאן היא **משחקים שהסתיימו**: ההעתקה נמצאת מחוץ ללולאת הצעדים, ומתבצעת פעם אחת אחרי כל C אפיזודות. זה גם המימוש שבו נשתמש בפרק הבא, וכך עושה גם המאמן במאגר Tic_Tac_Toe_DQN: רשת המטרה נוצרת שם כעותק של הראשית, ואחת ל־C אפוקים מועתקים אליה המשקלים באמצעות `load_state_dict`. אם בוחרים במקום זאת לספור C צעדי אימון, זו הגדרה אחרת של התדירות, וצריך לציין אותה במפורש. ערכי ההמשך מחושבים ברשת המטרה ללא גרדיאנט, והאופטימייזר מקבל רק את פרמטרי הרשת הראשית; כך אין עדכון עקיף של רשת המטרה. ובתחילת הריצה, כשהמאגר עדיין כמעט ריק, נהוג להמתין עד שיצטברו בו מספיק מעברים לאצווה שלמה לפני שמתחילים לאמן.

שימו לב שב־DQN רשת המטרה גם קובעת איזו פעולת המשך היא הטובה ביותר וגם נותנת את הערך שלה: ה־max עושה את שני הדברים בבת אחת. בחירת פעולת ההתנסות במשחק ממשיכה להיעשות ברשת הראשית עם ε-greedy. לעובדה שרשת אחת גם בוחרת וגם מעריכה נחזור בפרק על DDQN.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L63-L65] -->

כעת יש לנו את כל רכיבי DQN: רשת במקום טבלה, מאגר מעברים ורשת מטרה. בפרק הבא נחבר אותם לאימון סוכן באיקס עיגול, באמצעות ממשק המשחק הנתון.

<!-- editorlm-source-ref: [sources/RL/6.DQN.pptx#L71-L75] -->

<nav class="book-nav" aria-label="ניווט בספר">
<a href="10-TD%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="12-DQN%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">הבא ←</a>
</nav>

</div>

<!-- editorlm-source-versions: {"schemaVersion": 1, "sources": {"sources/RL/6.DQN.pptx": {"sourceSha256": "f38f194e9d775c359349d3aebcf6eaf8084daceb2dd6d449cc02c569631220f6", "canonicalTextSha256": "0e9158f31b0711094a167d1a805a5054fe4a4f62d288e407527d5f5f4dd507ac"}}} -->
