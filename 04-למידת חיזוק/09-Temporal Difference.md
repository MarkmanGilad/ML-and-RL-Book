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
.book .math-panel.highlight { background: #fff7d6; border: 2px solid #e0a800; }
.book .math-panel.highlight .katex { color: #9a3412; font-weight: bold; font-size: 1.25em; }
.book .math-panel p { margin: 0; }
.book .grid-panel { box-sizing:border-box; width:75%; max-width:75%; margin:20px auto; padding:16px 20px; background:#f3f6fa; border:1px solid #ccd7df; border-radius:8px; }
.book .grid { direction:ltr!important; width:auto!important; max-width:100%!important; margin:0 auto; border-collapse:collapse; background:#fff; }
.book .grid td { direction:ltr!important; text-align:center!important; width:64px; height:48px; border:1px solid #8199aa; }
.book .grid .goal { background:#d3efdc; } .book .grid .bad { background:#f4d7d7; }
</style>

<div class="book" dir="rtl" lang="he">

<nav class="book-nav" aria-label="ניווט בספר">
<a href="08-%D7%9E%D7%95%D7%A0%D7%98%D7%94%20%D7%A7%D7%A8%D7%9C%D7%95%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="10-TD%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">הבא ←</a>
</nav>

## ד.9 — <span dir="ltr" style="unicode-bidi:isolate">Temporal Difference</span>

<p style="text-align:center!important">שיטות במשפחת TD: <span dir="ltr" style="unicode-bidi:isolate">SARSA</span> ו־<span dir="ltr" style="unicode-bidi:isolate">Q-learning</span></p>

**המצגת:** [Temporal Difference](../../../sources/RL/5.%20Temporal%20Difference.pptx)

השאלה שהפרק הזה עונה עליה פשוטה: האם חייבים לחכות לסוף המשחק כדי ללמוד ממנו? בשני הפרקים הקודמים למדנו את שיטת מונטה קרלו: הסוכן משחק אפיזודה שלמה, מחכה לתוצאה הסופית, ורק אז חוזר אחורה ומעדכן את הערכים של כל המצבים והפעולות שעבר בדרך. השיטה עובדת יפה באיקס עיגול, כי המשחק מסתיים אחרי כמה מהלכים. אבל חשבו על נהג שלומד לנהוג: הוא אינו ממתין לסוף הנסיעה כדי להסיק שפנייה חדה מדי הייתה טעות. הוא מרגיש את התוצאה מיד ומתקן את הצעד הבא.

במשחק קצר אפשר להמתין לסיום כדי ללמוד מהתוצאה. אבל לגרסת מונטה קרלו שלמדנו, שמעדכנת רק בסוף האפיזודה, יש שלוש מגבלות:

- **אפיזודות ארוכות מאוד.** בשחמט עוברים עשרות מהלכים עד שמתקבל המצב הסופי, וכל הלמידה מהמשחק נדחית עד הסיום. ככל שהמסלול ארוך יותר, הלמידה איטית יותר, ובשחמט היא כמעט בלתי אפשרית.
- **תהליך ללא מצב סופי.** סוכן שמשקיע בבורסה פועל יום אחרי יום, ואין רגע שבו "המשחק נגמר" ואפשר לחשב תשואה. בלי מצב סופי אין אפיזודה שלמה, ומונטה קרלו אינו יכול לעדכן כלל.
- **לולאות.** גם במשחק שיש בו מצב סופי, הסוכן עלול להסתובב שוב ושוב בין אותם מצבים בלי להתקדם לסיום, ואז העדכון מתעכב בלי גבול.

**Temporal Difference — TD** מאפשרת לעדכן ערכים כבר אחרי צעד אחד: משתמשים בתגמול שהתקבל ובאומדן של מה שצפוי בהמשך.

הרעיון הכללי מחבר שני דברים שכבר ראינו. ממונטה קרלו לוקחים את הלמידה מדגימות: אין לנו מודל של הסביבה, ולכן לומדים מניסיון בפועל. מ־Value Iteration לוקחים את ה־Bootstrapping: במקום לחכות לתגמולים העתידיים, משתמשים בהערכה הקיימת של המצב הבא. השילוב נותן אלגוריתם שלומד מכל צעד בודד, בלי מודל ובלי המתנה.

בפרק נציג תחילה את עדכון TD הבסיסי לערכי מצבים, ואחר כך נעבור לערכי Q ולשני האלגוריתמים המרכזיים במשפחה: SARSA ו־Q-learning. ההבדל ביניהם דק אך חשוב, ונקדיש לו סעיף השוואה. בפרק הבא ניישם את הרעיון על איקס עיגול.

### עדכון בלי להמתין לסוף האפיזודה

נתחיל מהמקרה הפשוט ביותר: טבלה של ערכי מצבים V, כמו זו שהכרנו ב־Value Iteration. נזכיר שערך המצב V(S) הוא אומדן לסכום התגמולים המהוון שהסוכן צפוי לצבור מהמצב S והלאה. במונטה קרלו האומדן הזה התעדכן לכיוון התשואה G<sub>t</sub> שנמדדה עד סוף האפיזודה. ב־TD דוגמים את הסביבה בדיוק באותו אופן, משחקים ומקבלים תגמולים, אבל במקום להמתין לסוף האפיזודה מעדכנים את הערך מיד אחרי כל צעד. הדרך לעשות זאת היא בעזרת משוואת בלמן: ערך של מצב הוא התגמול המיידי ועוד הערך המהוון של המצב הבא. נראה עכשיו שהרעיון הזה יוצא ישירות מנוסחת מונטה קרלו, בכמה צעדים אלגבריים.

#### מנוסחת מונטה קרלו לנוסחת TD

**צעד 1 — נקודת המוצא.** זהו [כלל העדכון של מונטה קרלו](07-מונטה%20קרלו.md#return) לערך המצב S<sub>t</sub>. התשואה G<sub>t</sub> היא סכום התגמולים המהוון מהצעד t ועד סוף האפיזודה:

<div class="math-panel" dir="ltr">

$$
\begin{gathered} V(S_t) \leftarrow V(S_t) + \alpha \left[ G_t - V(S_t) \right] \\ G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \gamma^3 R_{t+3} + \cdots \end{gathered}
$$

</div>

**צעד 2 — מוציאים γ מחוץ לסוגריים.** כל האיברים מהשני והלאה מכילים לפחות γ אחד. נשאיר את התגמול הראשון R<sub>t</sub> בחוץ, ומשאר האיברים נוציא γ אחד החוצה:

<div class="math-panel" dir="ltr">

$$
G_t = R_t + \gamma \left( R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots \right)
$$

</div>

**צעד 3 — מזהים את הסוגריים.** הביטוי בסוגריים הוא בדיוק התשואה של הצעד הבא, G<sub>t+1</sub>: התגמול R<sub>t+1</sub> בלי היוון, אחריו R<sub>t+2</sub> כפול γ, וכן הלאה. קיבלנו קשר פשוט בין התשואה של צעד לתשואה של הצעד שאחריו:

<div class="math-panel" dir="ltr">

$$
G_t = R_t + \gamma G_{t+1}
$$

</div>

זו אותה נוסחה שבעזרתה חישבנו בפרק מונטה קרלו את התשואות מהסוף להתחלה, G = r + γ·G, רק שהפעם היא כתובה במפורש לצעד t.

**צעד 4 — הצעד של TD.** כאן הבעיה של מונטה קרלו נראית בבירור. ברגע שביצענו את הצעד מ־S<sub>t</sub> ל־S<sub>t+1</sub>, אנחנו כבר יודעים את R<sub>t</sub>. אבל G<sub>t+1</sub> עדיין אינו ידוע: הוא תלוי בכל מה שיקרה בהמשך המשחק, וזו בדיוק הסיבה שמונטה קרלו מחכה לסיום. אלא שיש לנו משהו במקומו. הטבלה כבר מכילה את V(S<sub>t+1</sub>), האומדן שלנו לתשואה הצפויה מהמצב הבא, כלומר בדיוק אומדן ל־G<sub>t+1</sub>. TD מחליף את התשואה העתידית, שעוד לא נמדדה, באומדן הזה:

<div class="math-panel" dir="ltr">

$$
G_t \approx R_t + \gamma V(S_{t+1})
$$

</div>

**צעד 5 — מציבים בנוסחת העדכון.** במקום G<sub>t</sub> כותבים את הביטוי החדש בתוך כלל העדכון של מונטה קרלו, ומקבלים את כלל העדכון של TD:

<div class="math-panel" dir="ltr">

$$
V(S_t) \leftarrow V(S_t) + \alpha \left[ R_t + \gamma V(S_{t+1}) - V(S_t) \right]
$$

</div>

זו המשמעות של V(S<sub>t</sub>) לפי TD: התגמול שהתקבל בצעד הזה, ועוד γ כפול הערך של המצב שאליו הגענו. זו בדיוק צורת [משוואת בלמן](05-Value%20Iteration.md#bootstrapping) שהכרנו ב־Value Iteration, בשני הבדלים: במקום לחשב תוחלת על כל המצבים הבאים לפי המודל, משתמשים במצב הבא היחיד שנדגם בפועל; ובמקום להחליף את הערך הישן בערך המחושב, מזיזים אותו רק חלק מהדרך, בעזרת α, כי דגימה אחת היא רק דגימה אחת.

**בדיקה במספרים.** ניקח את המשחק מפרק מונטה קרלו: X מנצח בשלושה צעדים, התגמולים הם 0, 0 ו־1, ו־γ=0.9. מהסוף להתחלה: <span dir="ltr">G<sub>2</sub> = 1</span>, ‏<span dir="ltr">G<sub>1</sub> = 0 + 0.9·1 = 0.9</span>, ‏<span dir="ltr">G<sub>0</sub> = 0 + 0.9·0.9 = 0.81</span>. נבדוק את צעד 3 מול הסכום המלא: <span dir="ltr">G<sub>0</sub> = 0 + 0.9·0 + 0.81·1 = 0.81</span>, אותו מספר. עכשיו נחשוב על TD: מיד אחרי הצעד הראשון עדיין איננו יודעים ש־G<sub>1</sub> יצא 0.9, כי המשחק נמשך. אם בטבלה כתוב כרגע <span dir="ltr">V(S<sub>1</sub>) = 0.6</span>, היעד של TD הוא <span dir="ltr">0 + 0.9·0.6 = 0.54</span>, ולא 0.81. ההפרש נובע מכך שהאומדן בטבלה עדיין אינו מדויק. ככל שהאימון מתקדם, V(S<sub>1</sub>) מתקרב לתשואה הממוצעת מהמצב הזה, ויעד TD מתקרב ליעד של מונטה קרלו. זהו המחיר של הלמידה המיידית: TD נשען על איכות הטבלה, והטבלה משתפרת תוך כדי.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L9-L23] -->

#### היעד והעדכון בכתיב הכללי

מכאן נכתוב את הנוסחה בקיצור, בלי אינדקס הזמן: המצב הנוכחי S, המצב הבא S′ והתגמול שהתקבל במעבר R. אחרי מעבר מ־S ל־S′ התגמולים הרחוקים עדיין אינם ידועים, אבל כבר יש לנו הערכה V(S′). לכן היעד משלב מידע שנמדד עכשיו עם הערכה לעתיד:

<div class="math-panel highlight" dir="ltr">

$$
\begin{gathered} \text{target} = R + \gamma V(S') \\ V(S) \leftarrow V(S) + \alpha \left[ \text{target} - V(S) \right] \end{gathered}
$$

</div>

השורה הראשונה מגדירה את **היעד — target**: מה שאנחנו חושבים כעת שערך המצב S צריך להיות. השורה השנייה מזיזה את הערך הישן חלק מהדרך לכיוון היעד. הפרמטר α הוא קצב הלמידה שהכרנו במונטה קרלו: α קטן מזיז את הערך מעט בכל עדכון, ו־α גדול נותן משקל רב לדגימה האחרונה. הפרמטר γ הוא מקדם ההיוון, שמקטין את משקלם של תגמולים רחוקים.

בניגוד ל־[תשואה מאפיזודה מלאה](07-מונטה%20קרלו.md#return), היעד הזה אינו סכום של כל התגמולים שכבר נצפו עד הסיום. החלק הראשון שלו הגיע מהסביבה, והחלק השני מגיע מטבלת הערכים הנוכחית.

<figure>
<img src="../assets/slides/31943ddd62/image6.png" alt="שני עצי משחק: במונטה קרלו מודגש מסלול שלם עד מצב סופי, ב־TD מודגש צעד אחד בלבד" style="width:100%;max-width:100%;height:auto;">
<figcaption>אותו עץ משחק מפרק מונטה קרלו. משמאל (MC): כדי לעדכן את S<sub>t</sub> מחכים למסלול שלם עד מצב סופי T. מימין (TD): מעדכנים כבר אחרי צעד אחד, לפי התגמול של הצעד (בתמונה מסומן r<sub>t+1</sub>; בסימון של הספר זהו R<sub>t</sub>) והאומדן הקיים של המצב הבא S<sub>t+1</sub>.</figcaption>
</figure>

לדוגמה, אם R=0, ‏γ=0.9 ו־V(S′)=0.8, היעד הוא 0.72. אם הערך הישן של S הוא 0.5 ו־α=0.1, נקבל ערך חדש 0.522. אפשר לבצע את העדכון מיד, גם אם המשחק נמשך עוד צעדים רבים. נשים לב שהערך זז רק מ־0.5 ל־0.522, אף שהיעד היה 0.72: זהו עדכון הדרגתי, ורק אחרי דגימות רבות הערך מתקרב ליעד.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L15-L23] -->

### TD Error ו־Bootstrapping

נחזור לנוסחת האימון של TD, הפעם בכתיב הכללי:

<div class="math-panel" dir="ltr">

$$
V(S) \leftarrow V(S) + \alpha \left[ R + \gamma V(S') - V(S) \right]
$$

</div>

הביטוי בסוגריים המרובעים הוא הפער בין היעד לבין הערך הנוכחי: מה שחשבנו שהמצב שווה, לעומת מה שמתברר עכשיו, אחרי צעד אחד. כדאי לתת לפער הזה שם. בספרות הוא נקרא **שגיאת TD — TD Error**, ומסמנים אותו באות היוונית δ (דלתא):

<div class="math-panel" dir="ltr">

$$
\delta = R + \gamma V(S') - V(S)
$$

</div>

עם הסימון הזה נוסחת האימון נכתבת בקיצור:

<div class="math-panel" dir="ltr">

$$
V(S) \leftarrow V(S) + \alpha \, \delta
$$

</div>

כלומר, בכל עדכון מוסיפים לערך הישן את השגיאה כפול קצב הלמידה. שגיאה חיובית אומרת שהמצב היה טוב יותר ממה שחשבנו, והערך עולה; שגיאה שלילית אומרת שהוא היה גרוע יותר, והערך יורד. כשהאומדן מדויק, השגיאה בממוצע קרובה לאפס והערכים מתייצבים. במצב סופי אין המשך, ולכן החלק העתידי מתאפס והיעד הוא R בלבד. את המונח שגיאת TD נפגוש שוב בפרק על DQN, שם הוא יהפוך לפונקציית ההפסד של רשת נוירונים.

נשים לב למה שקורה בתוך השגיאה: כדי לשפר את ההערכה של המצב הנוכחי V(S) משתמשים בהערכה של המצב הבא V(S′), שאותה קבענו בעצמנו, בטבלה שאנחנו בונים תוך כדי. זהו [Bootstrapping](05-Value%20Iteration.md#bootstrapping), אותו רעיון שפגשנו ב־Value Iteration. השם בא מהביטוי האנגלי "להרים את עצמך בלולאות המגף": האומדנים משפרים אומדנים, בלי לחכות למידע חיצוני מסוף האפיזודה.

<figure>
<img src="../assets/slides/31943ddd62/image7.png" alt="יד מושכת בלולאת המגף של נעל" style="width:45%;max-width:100%;height:auto;">
<figcaption>Bootstrapping: TD "מושך את עצמו" בעזרת הערכים שכבר יש לו בטבלה. ההערכה של המצב הבא, שהאלגוריתם עצמו קבע, משתתפת בשיפור ההערכה של המצב הנוכחי.</figcaption>
</figure>

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L25-L27] -->

### מטבלת V לטבלת Q

עד כאן דיברנו על ערכי מצבים. אבל כדי שהסוכן יבחר פעולה לפי V(S′) הוא צריך לדעת לאיזה מצב תוביל כל פעולה, כלומר מודל של הסביבה, ואת המודל הזה אין לנו. לכן, בדומה למונטה קרלו, כדי לבחור פעולות ללא מודל נשתמש ב־Q, מהסיבה שהוסברה ב־[מונטה קרלו](07-מונטה%20קרלו.md#mc-update): Q(S,A) אומר ישירות כמה שווה לבצע את הפעולה A במצב S, והסוכן בוחר את הפעולה בעלת הערך הגבוה, גם בלי לדעת לאן היא מובילה.

שני דברים מקבלים מהטבלה בלי מודל. הראשון הוא המדיניות: במצב s בוחרים את הפעולה שערכה הגבוה ביותר. השני הוא ערך המצב עצמו: אם במצב s נבחר את הפעולה הטובה ביותר, ערך המצב הוא ערך הפעולה הזאת:

<div class="math-panel" dir="ltr">

$$
\begin{gathered} \pi(s) = \arg\max_a Q(s,a) \\ V(s) = \max_a Q(s,a) \end{gathered}
$$

</div>

שימו לב להבדל בין השתיים, שכבר פגשנו ב־Value Iteration: argmax מחזירה את **הפעולה** שנותנת את המקסימום, ואילו max מחזירה את **הערך** המרבי עצמו. בשתיהן עוברים רק על הפעולות החוקיות במצב. הקשר השני חשוב לנו מיד: הוא אומר שאת V(S′) שביעד של TD אפשר להחליף בערך Q של המצב הבא.

**אותן נוסחאות שכתבנו ל־V חלות גם על Q.** היעד הוא התגמול ועוד γ כפול ערך ההמשך, והעדכון מזיז את הערך הישן חלק מהדרך אל היעד. ההבדל היחיד הוא שעכשיו הערכים נלקחים מטבלת Q: הערך שמעדכנים הוא Q(S,A) של המצב והפעולה שביצענו, וערך ההמשך הוא Q(S′,A′) של המצב הבא עם פעולה A′ שלו:

<div class="math-panel highlight" dir="ltr">

$$
\begin{gathered} \text{target} = R + \gamma Q(S',A') \\ Q(S,A) \leftarrow Q(S,A) + \alpha \left[ \text{target} - Q(S,A) \right] \end{gathered}
$$

</div>

גם שגיאת TD נכתבת באותו אופן, <span dir="ltr">δ = R + γQ(S′,A′) − Q(S,A)</span>, והעדכון הוא <span dir="ltr">Q(S,A) ← Q(S,A) + αδ</span>. נותרה שאלה אחת: למצב הבא יש כמה פעולות אפשריות, ולכל אחת ערך Q משלה. איזו A′ נכניס ליעד? השאלה הזאת מובילה לשני האלגוריתמים שבהמשך הפרק.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L25-L31] -->

### מונטה קרלו לעומת TD

לפני שנפרט את שני האלגוריתמים, נעמיד את שתי השיטות זו מול זו. במונטה קרלו העדכון נעשה לפי התשואה G<sub>t</sub> שנמדדה עד סוף האפיזודה, גם לטבלת V וגם לטבלת Q:

<div class="math-panel" dir="ltr">

$$
\begin{gathered} G_t = R_t + \gamma R_{t+1} + \gamma^2 R_{t+2} + \cdots \\ V(s) \leftarrow V(s) + \alpha \left[ G_t - V(s) \right] \\ Q(s,a) \leftarrow Q(s,a) + \alpha \left[ G_t - Q(s,a) \right] \end{gathered}
$$

</div>

ב־TD מחליפים את G<sub>t</sub> ביעד של צעד אחד, בעזרת Bootstrapping. בטבלת Q ערך ההמשך הוא ערך Q של המצב הבא s′ עם פעולה a′ שלו:

<div class="math-panel" dir="ltr">

$$
\begin{gathered} V(s) \leftarrow V(s) + \alpha \left[ R + \gamma V(s') - V(s) \right] \\ Q(s,a) \leftarrow Q(s,a) + \alpha \left[ R + \gamma Q(s',a') - Q(s,a) \right] \end{gathered}
$$

</div>

המבנה של ארבע הנוסחאות זהה: ערך ישן, ועוד α כפול ההפרש בין היעד לערך הישן. ההבדל כולו ביעד, ומהיעד נובעים כל ההבדלים המעשיים בין השיטות:

| | מונטה קרלו | TD |
| --- | --- | --- |
| מה צריך כדי לעדכן | אפיזודה שלמה, עד המצב הסופי | מעבר אחד: <span dir="ltr">S, A, R, S′</span> |
| מתי מעדכנים | בסוף האפיזודה, את כל המצבים שבמסלול | מיד אחרי כל צעד, מצב אחד |
| היעד | G<sub>t</sub>, התשואה שנמדדה בפועל | R ועוד γ כפול ערך משוער של המצב הבא |
| על מה היעד נשען | רק על תגמולים אמיתיים | על תגמול אמיתי אחד ועל אומדן מהטבלה |
| מה מגביל | אפיזודות ארוכות, תהליכים ללא סיום, לולאות | דיוק הטבלה בתחילת האימון |

בשתי השיטות דוגמים מסלול אחד ולא עוברים על כל הענפים, ולכן שתיהן Sample Backup. ההבדל הוא באורך המסלול שנדגם לפני העדכון: מסלול שלם לעומת צעד אחד. האם ההחלפה של תשואה אמיתית באומדן פוגעת בתוצאה הסופית? Sutton הראה ב־1988 שגם TD מתכנס לערכים הנכונים, בתנאים דומים לאלה של מונטה קרלו: מבקרים בכל המצבים שוב ושוב, וקצב הלמידה מתאים. בתנאים דומים גם עדכוני Q של TD מתכנסים ל־Q*, ערכי הפעולה של המדיניות המיטבית. כלומר, אפשר ללמוד את המדיניות הטובה ביותר צעד אחר צעד, בלי להמתין לסיום.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L33-L35] -->

### דגימת הסביבה

כמו במונטה קרלו, גם ב־TD אין לנו מודל של הסביבה. איננו יודעים מראש לאיזה מצב תוביל פעולה ומה יהיה התגמול, ולכן את המידע הזה משיגים בדגימה: הסוכן מבצע פעולה בפועל, והסביבה מחזירה לו את המצב הבא S′ ואת התגמול R. במונטה קרלו אספנו כך משחק שלם לפני העדכון; ב־TD דוגמים צעד אחד, מעדכנים, ודוגמים את הצעד הבא.

הדגימה מעלה שוב את השאלה שפגשנו במונטה קרלו: איזו פעולה לבצע? אם נבחר תמיד את הפעולה בעלת ה־Q הגבוה ביותר, נתקבע על מה שכבר נראה טוב, ולעולם לא נגלה פעולות טובות יותר שטרם ניסינו. זהו האיזון בין חקירה לניצול, Exploration מול Exploitation. הפתרון זהה לזה של מונטה קרלו: בוחרים פעולות לפי ε-greedy. בהסתברות ε מגרילים פעולה חוקית אקראית, וביתר המקרים בוחרים את הפעולה בעלת Q מרבי. בתחילת האימון ε גדול, כדי לחקור הרבה, והוא יורד בהדרגה ככל שהטבלה משתפרת, כפי שראינו ב־[דעיכת ε](07-מונטה%20קרלו.md#epsilon-decay). 

בספרות יש שני אלגוריתמים כמעט זהים שמשלבים את הדגימה הזאת עם עדכון TD: 
* SARSA
* Q-learning.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L37-L39] -->

<a id="sarsa"></a>
### SARSA

באלגוריתם SARSA אנחנו מאמנים את הסוכן לפי השלבים הבאים. הסוכן נמצא באמצע משחק, ובכל צעד הוא מבצע ארבעה שלבים:

1. **מקבלים מצב S.** זהו המצב שבו הסוכן נמצא עכשיו.
2. **בוחרים פעולה A לפי ε-greedy.** מסתכלים בטבלת Q בשורה של S ובוחרים: לרוב את הפעולה בעלת הערך הגבוה, ולפעמים פעולה אקראית.
3. **משחקים ומקבלים מהסביבה את S′ ו־R.** מבצעים את A, והסביבה מחזירה את המצב הבא ואת התגמול.
4. **בוחרים לפי ε-greedy את הפעולה הבאה A′.** מסתכלים בטבלת Q בשורה של S′ ובוחרים, באותה שיטה, את הפעולה שתבוצע שם.

בסוף ארבעת השלבים יש בידינו חמישה דברים: <strong><span dir="ltr">S, A, R, S′, A′</span></strong>. ראשי התיבות שלהם הם שם האלגוריתם: SARSA. עכשיו נסתכל שוב בנוסחת העדכון של Q, ונצבע באדום את מה שכבר בידינו:

<div class="math-panel" dir="ltr">

$$
Q(\textcolor{#c00000}{S},\textcolor{#c00000}{A}) \leftarrow Q(\textcolor{#c00000}{S},\textcolor{#c00000}{A}) + \alpha \left[ \textcolor{#c00000}{R} + \gamma Q(\textcolor{#c00000}{S'},\textcolor{#c00000}{A'}) - Q(\textcolor{#c00000}{S},\textcolor{#c00000}{A}) \right]
$$

</div>

כל מה שמופיע בנוסחה כבר ידוע: S ו־A משלבים 1 ו־2, R ו־S′ משלב 3, A′ משלב 4, והערכים Q(S,A) ו־Q(S′,A′) נמצאים בטבלה. אפשר לעדכן מיד, בלי לחכות לסוף המשחק.

את ארבעת השלבים והעדכון עושים **בלולאה**, עד סוף האפיזודה. יש כאן פרט חשוב: הפעולה הבאה A′ כבר נבחרה בשלב 4, ולכן בסיבוב הבא לא בוחרים פעולה מחדש. המצב הבא הופך למצב הנוכחי (<span dir="ltr">S ← S′</span>), הפעולה שנבחרה הופכת לפעולה הנוכחית (<span dir="ltr">A ← A′</span>), וממשיכים ישר לשלב 3: משחקים אותה. במצב סופי אין המשך ואין A′; היעד הוא R בלבד, והאפיזודה מסתיימת.

הפסאודו־קוד מסכם את הלולאה:

<div class="code-panel" dir="ltr">
<pre><code>Initialize Q
For each episode:
    Initialize S
    Choose A using epsilon-greedy
    Repeat:
        Perform A and observe R, S'
        If S' is terminal:
            target = R
        Else:
            Choose A' using epsilon-greedy
            target = R + gamma * Q(S', A')
        Q(S, A) += alpha * (target - Q(S, A))
        If S' is terminal: stop this episode
        S = S'
        A = A'
</code></pre>
</div>

שימו לב לשלושה דברים בקוד. הפעולה הראשונה של כל אפיזודה נבחרת לפני הלולאה, ובתוך הלולאה בוחרים רק את A′. הענף של המצב הסופי מעדכן לפי R בלבד. ובסוף כל סיבוב שתי ההשמות <span dir="ltr">S = S′</span> ו־<span dir="ltr">A = A′</span> מעבירות את הזוג הבא לסיבוב הבא, כך שהפעולה שנכנסה ליעד היא גם הפעולה שתבוצע בפועל. בגלל התכונה הזאת SARSA נקרא **on-policy**: הוא לומד את הערכים של המדיניות שמשחקת בפועל, כולל בחירות החקירה שלה.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L41-L47] -->

<a id="q-learning"></a>
### Q-learning

באלגוריתם Q-learning מאמנים את הסוכן לפי אותם ארבעה שלבים, וההבדל היחיד מסומן באדום:

1. **מקבלים מצב S.**
2. **בוחרים פעולה A לפי ε-greedy.**
3. **משחקים ומקבלים מהסביבה את S′ ו־R.**
4. <span style="color:#c00000;font-weight:bold">**בוחרים את הפעולה הבאה A′ לפי הערך המרבי בטבלת Q, בלי ε.**</span> מסתכלים בטבלת Q בשורה של S′ ולוקחים את הפעולה בעלת הערך הגבוה ביותר.

ב־SARSA בחרנו את A′ לפי ε-greedy, כלומר לפעמים באקראי. ב־Q-learning לא מגרילים: לצורך העדכון לוקחים תמיד את הטוב ביותר, ולכן ליעד נכנס הערך המרבי בשורה של S′. גם בנוסחה ההבדל היחיד מסומן באדום:

<div class="math-panel" dir="ltr">

$$
Q(S,A) \leftarrow Q(S,A) + \alpha \left[ R + \gamma \, \textcolor{#c00000}{\max_{a'} Q(S',a')} - Q(S,A) \right]
$$

</div>

המקסימום הוא על הפעולות החוקיות במצב S′. ואם ליעד נכנס תמיד הערך המרבי, אין צורך לשמור את A′ לסיבוב הבא: בתחילת כל סיבוב בוחרים מחדש, לפי ε-greedy, את הפעולה שמבצעים בפועל. הסוכן ממשיך לחקור במשחק, אבל היעד מניח שבהמשך ייבחר הטוב ביותר. בפסאודו־קוד השורות שהשתנו לעומת SARSA מסומנות באדום:

<div class="code-panel" dir="ltr">
<pre><code>Initialize Q
For each episode:
    Initialize S
    Repeat:
        <span style="color:#c00000;font-weight:bold">Choose A using epsilon-greedy</span>
        Perform A and observe R, S'
        If S' is terminal:
            target = R
        Else:
            <span style="color:#c00000;font-weight:bold">target = R + gamma * max Q(S', legal action)</span>
        Q(S, A) += alpha * (target - Q(S, A))
        S = S'
    Until S is terminal
</code></pre>
</div>

בחירת הפעולה עברה לתוך הלולאה, ליעד נכנס המקסימום, ושורת <span dir="ltr">A = A′</span> נעלמה. תרשימי הזרימה של שני האלגוריתמים מראים שזה כל ההבדל:

<figure>
<img src="../assets/rl/td/sarsa-vs-qlearning.svg" alt="שני תרשימי זרימה זה לצד זה: Q-learning משמאל עם עדכון לפי gamma max Q, ו־SARSA מימין עם שלב נוסף, מוקף באדום, של בחירת a′ ב־epsilon-greedy לפני העדכון" style="width:100%;max-width:100%;height:auto;">
<figcaption>תרשימי הזרימה של שני האלגוריתמים (שרטוט מחדש של התרשים מתוך <a href="https://www.oreilly.com/library/view/hands-on-reinforcement-learning/9781788836524/20659243-cadb-46f0-b5c3-3acadd590d67.xhtml">Hands-On Reinforcement Learning</a>, O'Reilly). משמאל Q-learning: בוחרים a ב־ε-greedy, מבצעים, ומעדכנים לפי γ·max Q(s′,a), המסומן במסגרת אדומה. מימין SARSA: בין הביצוע לעדכון יש שלב נוסף, מוקף באדום, בחירת a′ במצב s′ ב־ε-greedy, והעדכון משתמש ב־γ·Q(s′,a′). התרשים אינו מציג את ההעברה <span dir="ltr">S←S′</span> ו־<span dir="ltr">A←A′</span>; לסדר המדויק היצמדו לפסאודו־קוד.</figcaption>
</figure>

**דוגמה במספרים.** נניח שבמצב הבא יש שתי פעולות בעלות ערכים 0.8 ו־0.2, והחקירה בחרה בפעולה השנייה. עבור R=0 ו־γ=0.9, יעד SARSA יהיה 0.18 (כי <span dir="ltr">0.9·0.2</span>) ואילו יעד Q-learning יהיה 0.72 (כי <span dir="ltr">0.9·0.8</span>). המעבר שנדגם זהה, וההפרש נובע רק מהבחירה בשלב 4. SARSA "מעניש" את המצב הנוכחי על כך שהחקירה עלולה לבחור בו פעולה גרועה; Q-learning מתעלם מהחקירה.

לכן Q-learning נקרא **off-policy**: הסוכן משחק במדיניות אחת, עם חקירה, ולומד את הערכים של מדיניות אחרת, החמדנית, בלי חקירה. התכונה הזאת תאפשר בהמשך ללמוד גם מדגימות ישנות שנשמרו בזיכרון, ונחזור אליה בפרק על DQN. אין מכאן מסקנה שאחד האלגוריתמים תמיד טוב יותר; מה שחשוב הוא לא לערבב ביניהם. טעות נפוצה במימוש היא לבחור A′ ב־ε-greedy לצורך היעד, ואז להגריל פעולה חדשה לצעד הבא. זה אינו SARSA ואינו Q-learning.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L49-L67] -->

### n-step TD — כמה צעדים לפני האומדן

עד עכשיו עמדו לפנינו שני קצוות: מונטה קרלו, שמחכה עד סוף האפיזודה ומשתמש רק בתגמולים אמיתיים, ו־TD של צעד אחד, שמשתמש בתגמול יחיד ומיד עובר לאומדן. בספרות TD של צעד אחד מכונה גם TD(0), וכך הוא מסומן בתמונה שלמטה. בין שני הקצוות יש רצף שלם של אפשרויות ביניים. אפשר להמתין לשניים או לשלושה צעדים לפני שמשתמשים באומדן ההמשך. כך משלבים יותר תגמולים שנמדדו בפועל עם ערך משוער בקצה המסלול. עבור n מעברים, באותו סימון של הפרק, שבו R<sub>t</sub> הוא התגמול שאחרי הפעולה בזמן t, היעד הוא:

<div class="math-panel" dir="ltr">

$$
G_t^{(n)} = R_t + \gamma R_{t+1} + \cdots + \gamma^{n-1} R_{t+n-1} + \gamma^n V(S_{t+n})
$$

</div>

למשל, ב־2-step נשתמש בשני תגמולים ואז בערך המצב שאליו הגענו: <span dir="ltr">R<sub>t</sub> + γR<sub>t+1</sub> + γ²V(S<sub>t+2</sub>)</span>. את V(S<sub>t</sub>) נעדכן לכיוון היעד הזה בעזרת α, באותו מבנה של עדכון הדרגתי.

<figure>
<img src="../assets/slides/31943ddd62/image18.png" alt="עמודות של מצבים ופעולות באורך גדל: צעד אחד, שני צעדים, שלושה, n צעדים ועד מונטה קרלו" style="width:80%;max-width:100%;height:auto;">
<figcaption>הרצף בין השיטות. בכל עמודה עיגול הוא מצב ונקודה היא פעולה. TD של צעד אחד, TD(0), משתמש בתגמול אחד ואז באומדן של המצב האחרון בעמודה; 2-step ו־3-step משתמשים ביותר תגמולים שנמדדו בפועל לפני האומדן; בקצה הימני, מונטה קרלו ממתין עד המצב הסופי (הריבוע) ואינו משתמש באומדן כלל.</figcaption>
</figure>

אם האפיזודה מסתיימת לפני שנאספו n צעדים, עוצרים בסיום ואינם מוסיפים ערך עתידי. כשנאסף צעד יחיד מתקבל TD של צעד אחד; כשמחכים עד סוף האפיזודה ומשתמשים רק בתגמולים, חוזרים לרעיון של מונטה קרלו. n גדול יותר מכניס ליעד יותר מידע שנמדד בפועל ופחות תלות באומדן, אך מחייב להמתין יותר לפני העדכון. בספר זה נסתפק ב־TD של צעד אחד.

בפרק הבא ניישם SARSA על איקס עיגול כשהסוכן משחק X. שם נתמקד במשמעות של צעד אחד מול יריב, בטיפול המדויק בסיום המשחק, ובטבלת AfterState שמחליפה את טבלת Q. המשימות שיישארו לכם: לממש Q-learning באותו משחק, ולהפעיל את אחד האלגוריתמים על השחקן O.

<!-- editorlm-source-ref: [sources/RL/5. Temporal Difference.pptx#L69-L77] -->

<nav class="book-nav" aria-label="ניווט בספר">
<a href="08-%D7%9E%D7%95%D7%A0%D7%98%D7%94%20%D7%A7%D7%A8%D7%9C%D7%95%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="10-TD%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md">הבא ←</a>
</nav>

</div>

<!-- editorlm-source-versions: {"schemaVersion": 1, "sources": {"sources/RL/5. Temporal Difference.pptx": {"sourceSha256": "e60d96da1e7a790024fd038cd0a4b569cbfd4d2e39fc26920472cc6ced05d99f", "canonicalTextSha256": "d847ef1583229bd8731218070d9870debc7edfd809f55780d7af70628fd35148"}}} -->
