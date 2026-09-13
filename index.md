<!-- editorlm-hebrew-html-start -->
<style>
html, body, .vscode-body, .markdown-body, .markdown-preview {
  direction: rtl !important; text-align: right !important;
}
.book { box-sizing: border-box; max-width: 960px; margin: auto; padding: 24px;
  background: #ffffff; color: #183b50; font-family: Arial, sans-serif; line-height: 1.8; }
.book p, .book ul, .book ol, .book li, .book h1, .book h2, .book h3, .book th, .book td {
  direction: rtl !important; text-align: right !important; unicode-bidi: isolate;
}
.book a { color: #176f78; text-underline-offset: 4px; }
.book a:focus-visible { outline: 3px solid #239b91; outline-offset: 4px; }
.book ul { padding-right: 24px; padding-left: 0; }
.book li { margin: 7px 0; }
.book h1 { font-size: 32px; border: 0; margin: 40px 0 20px; }
.book h3 { font-size: 23px; color: #174e49; border: 0; border-right: 4px solid #299c91;
  padding: 8px 16px; margin: 32px 0 16px; background: #eff7f5; border-radius: 5px; }
.book .cover { padding: 44px 40px; margin: 0 0 24px; border-radius: 14px;
  border-top: 6px solid #38bdb0; background: #112e43; color: #ffffff; }
.book .cover .eyebrow { color: #91e1d6; font-size: 14px; }
.book .cover h1 { color: #ffffff; font-size: 46px; line-height: 1.25; margin: 18px 0 12px; }
.book .cover .subtitle { color: #d4e6ed; font-size: 24px; }
.book .cover .author { font-size: 23px; margin-top: 30px; }
.book .cover .audience { color: #bcd4df; font-size: 15px; margin-top: 4px; }
.book .book-nav { display: flex; flex-wrap: wrap; gap: 10px; margin: 18px 0 34px; }
.book .book-nav a { padding: 9px 18px; border: 1px solid #cbdde3; border-radius: 8px;
  text-decoration: none; color: #183b50; background: #f3f7fa; font-weight: bold; }
.book .book-nav a.toc-link { background: #174e49; border-color: #174e49; color: #ffffff; }
.book .course-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; margin: 20px 0; }
.book .course-card { display: block; padding: 20px; border: 1px solid #d4e3e9; border-radius: 10px;
  background: #f4f8fb; text-decoration: none; color: #153b56; }
.book .course-card strong { display: block; font-size: 21px; margin-bottom: 5px; }
.book .course-card span { display: block; font-size: 15px; color: #496576; }
.book .course-card:hover { border-color: #299c91; background: #edf7f5; }
.book .resource-box { border: 1px solid #dbe6eb; border-radius: 10px; padding: 6px 22px 18px; margin: 18px 0; }
.book .resource-box h3 { background: transparent; padding: 0; border: 0; margin: 16px 0 10px; font-size: 21px; }
.book .note { padding: 14px 18px; background: #edf7f5; border-right: 4px solid #299c91; border-radius: 5px; font-size: 15px; }
.book code { direction: ltr; unicode-bidi: isolate; }
@media (max-width: 600px) {
  .book { padding: 12px; }
  .book .cover { padding: 30px 24px; }
  .book .cover h1 { font-size: 34px; }
  .book .course-grid { grid-template-columns: 1fr; }
}
@media print {
  .book { max-width: none; padding: 0; }
  .book .cover { break-after: page; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .book .book-nav { display: none; }
  .book .course-card, .book .resource-box { break-inside: avoid; }
  .book h1, .book h3 { break-after: avoid; }
}
</style>
<!-- editorlm-hebrew-html-end -->

<div class="book" dir="rtl" lang="he">

<div class="cover">
<div class="eyebrow">לחשוב · לתכנת · ללמוד</div>
<h1>למידת מכונה<br>ולמידת חיזוק</h1>
<div class="subtitle">באמצעות בניית משחקים</div>
<div class="author">גלעד מרקמן</div>
<div class="audience">ספר לימוד לתלמידי י״א–י״ב</div>
</div>

<nav class="book-nav" aria-label="ניווט בספר">
<a class="toc-link" href="#book-toc">תוכן העניינים</a>
<a href="#course-materials">אתר הקורס וחומרי ליווי</a>
<a href="01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/01-%D7%9E%D7%91%D7%95%D7%90.md">מתחילים לקרוא ←</a>
</nav>

<a id="course-materials"></a>

### אתר הקורס וחומרי ליווי

הספר מלווה את הקורס של **גלעד מרקמן — תכנות באינטרנט**. בכל מדור תמצאו את השיעורים, ההרצאות המוקלטות וחומרי הליווי המתאימים.

<div class="course-grid">
<a class="course-card" href="https://webprogramming.azurewebsites.net/Pages/Python/Installation.aspx"><strong>א · פייתון</strong><span>יסודות התכנות וסביבת העבודה</span></a>
<a class="course-card" href="https://webprogramming.azurewebsites.net/Pages/PyGame/MDP_Intro.aspx"><strong>ב · pygame</strong><span>חומרי הקורס המקוריים: Pygame ומשחקים</span></a>
<a class="course-card" href="https://webprogramming.azurewebsites.net/Pages/PyTorch/Intro.aspx"><strong>ג · למידת מכונה</strong><span>נתונים, אימון ורשתות נוירונים עם PyTorch</span></a>
<a class="course-card" href="https://webprogramming.azurewebsites.net/Pages/RL/RL_Intro.aspx"><strong>ד · למידת חיזוק</strong><span>MDP, מדיניות ולמידה מתוך תגמולים</span></a>
</div>

<div class="resource-box">

### מחברות ודוגמאות קוד

באתר הקורס יש מחברות Colab נוספות ודוגמאות קוד. קישורים ספציפיים מופיעים בדפי השיעורים, בפרקים המתאימים בספר ובמחברות הליווי.

[מאגרי הקוד של גלעד מרקמן ב־GitHub](https://github.com/MarkmanGilad) · [מחברות פייתון של האוניברסיטה הפתוחה](https://drive.google.com/drive/folders/1yLN-J12Mq3KZ0i6XJwpaA3XMC6xoh4GJ?usp=sharing)

</div>

<p class="note">בחלק א עובדים ב־Colab. ההתקנה המקומית של פייתון ו־VS Code תשמש בהמשך, בחלק ב. מחברות וחומרי ליווי נוספים מקושרים בראש הפרקים המתאימים.</p>

<a id="book-toc"></a>

# תוכן העניינים

### חלק א — פייתון

- [א.1 — מהי פייתון?](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/01-%D7%9E%D7%91%D7%95%D7%90.md)
- [א.2 — סביבת העבודה: Google Colab](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/02-%D7%A1%D7%91%D7%99%D7%91%D7%AA%20%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.md)
- [א.3 — פקודות בסיסיות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/03-%D7%A4%D7%A7%D7%95%D7%93%D7%95%D7%AA%20%D7%91%D7%A1%D7%99%D7%A1%D7%99%D7%95%D7%AA.md)
- [א.4 — מחרוזות — עבודה עם טקסט](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/04-%D7%9E%D7%97%D7%A8%D7%95%D7%96%D7%95%D7%AA.md)
- [א.5 — תנאים ובקרת זרימה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/05-%D7%AA%D7%A0%D7%90%D7%99%D7%9D.md)
- [א.6 — לולאות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/06-%D7%9C%D7%95%D7%9C%D7%90%D7%95%D7%AA.md)
- [א.7 — פונקציות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/07-%D7%A4%D7%95%D7%A0%D7%A7%D7%A6%D7%99%D7%95%D7%AA.md)
- [א.8 — רשימות — List](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/08-List.md)
- [א.9 — tuple](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/09-tuple.md)
- [א.10 — שוויון, זהות והעתקה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/10-%D7%A9%D7%95%D7%95%D7%99%D7%95%D7%9F%20%D7%95%D7%96%D7%94%D7%95%D7%AA.md)
- [א.11 — מילונים — dict](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/11-dict.md)
- [א.12 — קבוצות — set](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/12-set.md)
- [א.13 — חריגות — טיפול בשגיאות בזמן ריצה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/13-%D7%97%D7%A8%D7%99%D7%92%D7%95%D7%AA.md)
- [א.14 — רקורסיה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/14-%D7%A8%D7%A7%D7%95%D7%A8%D7%A1%D7%99%D7%94.md)
- [א.15 — חיפוש, מיון ויעילות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/15-%D7%97%D7%99%D7%A4%D7%95%D7%A9%20%D7%95%D7%9E%D7%99%D7%95%D7%9F.md)
- [א.16 — מחלקות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/16-%D7%9E%D7%97%D7%9C%D7%A7%D7%95%D7%AA.md)
- [א.17 — ירושה והכלה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/17-%D7%99%D7%A8%D7%95%D7%A9%D7%94.md)
- [א.18 — קבצים — קריאה וכתיבה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/18-%D7%A7%D7%91%D7%A6%D7%99%D7%9D.md)
- [א.19 — NumPy — מערכים, צורה וחיתוך](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/19-NumPy%20%D7%9E%D7%A2%D7%A8%D7%9B%D7%99%D7%9D.md)
- [א.20 — NumPy — חישובים ופעולות על מערכים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/20-NumPy%20%D7%97%D7%99%D7%A9%D7%95%D7%91%D7%99%D7%9D.md)
- [א.21 — PyPlot — גרפים ותרשימים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/21-PyPlot.md)
- [א.22 — תמונות כמערכים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/22-%D7%AA%D7%9E%D7%95%D7%A0%D7%95%D7%AA%20%D7%9B%D7%9E%D7%A2%D7%A8%D7%9B%D7%99%D7%9D.md)
- [א.23 — Pandas — סדרות וטבלאות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/23-Pandas%20%D7%98%D7%91%D7%9C%D7%90%D7%95%D7%AA.md)
- [א.24 — Pandas — ניקוי, קיבוץ וניתוח נתונים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/24-Pandas%20%D7%A0%D7%99%D7%AA%D7%95%D7%97%20%D7%A0%D7%AA%D7%95%D7%A0%D7%99%D7%9D.md)

### חלק ב — pygame

- [ב.1 — מעבר מ־Colab לעבודה מקומית](02-pygame/01-%D7%94%D7%AA%D7%A7%D7%A0%D7%94%20%D7%9E%D7%A7%D7%95%D7%9E%D7%99%D7%AA.md)
- [ב.2 — מבנה הלולאה הראשית](02-pygame/02-%D7%94%D7%9C%D7%95%D7%9C%D7%90%D7%94%20%D7%94%D7%A8%D7%90%D7%A9%D7%99%D7%AA.md)
- [ב.3 — אירועים וסגירת החלון](02-pygame/03-%D7%90%D7%99%D7%A8%D7%95%D7%A2%D7%99%D7%9D%20%D7%95%D7%A1%D7%92%D7%99%D7%A8%D7%94.md)
- [ב.4 — שעון, קצב פריימים ורענון המסך](02-pygame/04-%D7%A9%D7%A2%D7%95%D7%9F%20%D7%95%D7%A8%D7%A2%D7%A0%D7%95%D7%9F.md)
- [ב.5 — משטחים, שכבות וצבעים](02-pygame/05-%D7%9E%D7%A9%D7%98%D7%97%D7%99%D7%9D%20%D7%95%D7%A6%D7%91%D7%A2%D7%99%D7%9D.md)
- [ב.6 — ציור צורות גאומטריות](02-pygame/06-%D7%A6%D7%95%D7%A8%D7%95%D7%AA%20%D7%92%D7%90%D7%95%D7%9E%D7%98%D7%A8%D7%99%D7%95%D7%AA.md)
- [ב.7 — טעינה והצגה של תמונות](02-pygame/07-%D7%AA%D7%9E%D7%95%D7%A0%D7%95%D7%AA.md)
- [ב.8 — אינטראקציה עם המשתמש: עכבר ומקלדת](02-pygame/08-%D7%9E%D7%A7%D7%9C%D7%93%D7%AA%20%D7%95%D7%A2%D7%9B%D7%91%D7%A8.md)
- [ב.9 — אנימציה פשוטה](02-pygame/09-%D7%90%D7%A0%D7%99%D7%9E%D7%A6%D7%99%D7%94.md)
- [ב.10 — מלבני מיקום: pygame.Rect](02-pygame/10-Rect.md)
- [ב.11 — ספרייטים: pygame.sprite.Sprite](02-pygame/11-Sprite.md)
- [ב.12 — גילוי התנגשויות](02-pygame/12-%D7%94%D7%AA%D7%A0%D7%92%D7%A9%D7%95%D7%99%D7%95%D7%AA.md)
- [ב.13 — קבוצות ספרייטים והתנגשויות בין קבוצות](02-pygame/13-%D7%A7%D7%91%D7%95%D7%A6%D7%95%D7%AA%20%D7%A1%D7%A4%D7%A8%D7%99%D7%99%D7%98%D7%99%D7%9D.md)

### חלק ג — למידת מכונה

כל פרק מוסיף צעד אחד: מן הנתונים והנגזרות, דרך אימון ונרמול, ועד רשתות וסיווג תמונות.

- [ג.1 — מהי למידת מכונה?](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/01-%D7%9E%D7%91%D7%95%D7%90.md)
- [ג.2 — הכנת PyTorch ב־Colab](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/02-%D7%94%D7%AA%D7%A7%D7%A0%D7%AA%20PyTorch.md)
- [ג.3 — טנסורים ב־PyTorch](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/03-%D7%98%D7%A0%D7%A1%D7%95%D7%A8%D7%99%D7%9D.md)
- [ג.4 — נגזרות ו־Autograd](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/04-Autograd.md)
- [ג.5 — Gradient Descent במשתנה אחד](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/05-Gradient%20Descent%20%D7%91%D7%9E%D7%A9%D7%AA%D7%A0%D7%94%20%D7%90%D7%97%D7%93.md)
- [ג.6 — Gradient Descent בשני משתנים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/06-Gradient%20Descent%20%D7%91%D7%A9%D7%A0%D7%99%20%D7%9E%D7%A9%D7%AA%D7%A0%D7%99%D7%9D.md)
- [ג.7 — רגרסיה לינארית — משקל אחד](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/07-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99%D7%AA.md)
- [ג.8 — רגרסיה עם הטיה ו־nn.Linear](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/08-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%A2%D7%9D%20%D7%94%D7%98%D7%99%D7%94%20%D7%95-nn.Linear.md)
- [ג.9 — רגרסיה לינארית וחשיבות נרמול הנתונים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/09-%D7%A0%D7%A8%D7%9E%D7%95%D7%9C%20%D7%A0%D7%AA%D7%95%D7%A0%D7%99%D7%9D.md)
- [ג.10 — רגרסיה לינארית במספר משתנים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/10-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%91%D7%9E%D7%A1%D7%A4%D7%A8%20%D7%9E%D7%A9%D7%AA%D7%A0%D7%99%D7%9D.md)
- [ג.11 — גלטון — הכנת טבלה וחיזוי גובה](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/11-%D7%92%D7%9C%D7%98%D7%95%D7%9F%20-%20%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9E%D7%98%D7%91%D7%9C%D7%94.md)
- [ג.12 — רגרסיה לוגית ופונקציות אקטיבציה](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/12-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%95%D7%92%D7%99%D7%AA.md)
- [ג.13 — רשת נוירונים — זיהוי הספרה 7](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/13-%D7%A8%D7%A9%D7%AA%20%D7%A0%D7%95%D7%99%D7%A8%D7%95%D7%A0%D7%99%D7%9D%20ANN.md)
- [ג.14 — מגבלות הקו הישר ורגרסיה באמצעות רשת](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/14-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%90%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99%D7%AA.md)
- [ג.15 — Moon — ללמוד גבול סיווג שאינו ישר](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/15-Moon%20-%20%D7%A1%D7%99%D7%95%D7%95%D7%92%20%D7%9C%D7%90%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99.md)
- [ג.16 — סיווג בינארי של בגדים ואותיות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/16-%D7%A1%D7%99%D7%95%D7%95%D7%92%20%D7%91%D7%92%D7%93%D7%99%D7%9D%20%D7%95%D7%90%D7%95%D7%AA%D7%99%D7%95%D7%AA.md)
- [ג.17 — רשת במחלקה — סיווג עשר ספרות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/17-%D7%A8%D7%A9%D7%AA%20%D7%91%D7%90%D7%9E%D7%A6%D7%A2%D7%95%D7%AA%20%D7%9E%D7%97%D7%9C%D7%A7%D7%94.md)
- [ג.18 — סיווג רב־קטגוריות — Iris ו־Fashion-MNIST](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/18-%D7%A1%D7%99%D7%95%D7%95%D7%92%20%D7%A8%D7%91%20%D7%A7%D7%98%D7%92%D7%95%D7%A8%D7%99%D7%95%D7%AA.md)
- [ג.19 — Pima — השוואת רשתות לנתונים בטבלה](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/19-Pima%20-%20%D7%A8%D7%A9%D7%AA%20%D7%9C%D7%98%D7%91%D7%9C%D7%94.md)
- [ג.20 — שמירה וטעינה של מודלים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/20-%D7%A9%D7%9E%D7%99%D7%A8%D7%94%20%D7%95%D7%98%D7%A2%D7%99%D7%A0%D7%94.md)
- [ג.21 — רשתות קונבולוציה — CNN ו־CIFAR-10](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/21-%D7%A8%D7%A9%D7%AA%D7%95%D7%AA%20%D7%A7%D7%95%D7%A0%D7%91%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94.md)
- [ג.22 — חתול או לא חתול — CNN לסיווג בינארי](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/22-%D7%97%D7%AA%D7%95%D7%9C%20%D7%90%D7%95%20%D7%9C%D7%90%20%D7%97%D7%AA%D7%95%D7%9C.md)

- מעקב והשוואת ניסויי אימון עם W&B — פרק מתוכנן; ייכתב לאחר עיבוד מקורותיו.

### חלק ד — למידת חיזוק

הפרקים יתווספו בהמשך.


<nav class="book-nav" aria-label="ניווט בספר">
<a class="toc-link" href="#book-toc">תוכן העניינים</a>
<a href="#course-materials">אתר הקורס וחומרי ליווי</a>
<a href="01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/01-%D7%9E%D7%91%D7%95%D7%90.md">מתחילים לקרוא ←</a>
</nav>

</div>

<!-- editorlm-source-versions: {"schemaVersion":1,"sources":{"sources/Python/Python_Intro_Colab.pptx":{"sourceSha256":"6661ef452ccbf6f70f9e9d413207d0f16914ac4da9a38026e817f7e8d932658c","canonicalTextSha256":"2cca9ddeeb2f1c940efaadd82221ebda54fb08e2814fd46db348a62cdc164917"},"sources/Python/Python_Basic.pptx":{"sourceSha256":"32a2d56f6cb0e1eacf4a8a28f14d7932648610f4248f7178dae91b80b6ef7e84","canonicalTextSha256":"0a301b7608d0440e9cfaab4e39bd7bbb9518eaf76710de862723aa719cc60e4a"},"sources/Python/converted/1.Python_Basic/notebook.md":{"sourceSha256":"2d605efefadda4ead3844d4ae7e8066d8443ea6927868f6b4ca26a4bdc66d16c","canonicalTextSha256":"2d605efefadda4ead3844d4ae7e8066d8443ea6927868f6b4ca26a4bdc66d16c"},"sources/Python/Python_Classes_Inheritance.pptx":{"sourceSha256":"ad085713a21c8b50a6210c1b43f31e3421aad37238c20ec5a6c78825cf178af4","canonicalTextSha256":"09ec2e29ca4c246d64556136e69fee1eeac8a6234f55b06dac6d77cecd09e7e5"},"sources/Python/Python_Data_Strucrures.pptx":{"sourceSha256":"af0d66fc064d82bd80d368b0e9d39716f653abe73240936a8fce03b3ad2ff283","canonicalTextSha256":"80dd4b6c86b82109570ee1c3b0062963aab08de123e173c90e0967af586bfee4"},"sources/Python/Python_Numpy.pptx":{"sourceSha256":"d1a86b84fd49ca2baee3a81586a78246cf31d582742844b229c2f8f576d52fa3","canonicalTextSha256":"fe990439bdef892516fa8983a16f5eed04168924c84b6e9d819b5a94be5ca314"},"sources/Python/Python_PyPlot.pptx":{"sourceSha256":"01cadb34d9c969eeb2e63490275e6f56122c7ce9f3d9f193296e1e796656d85b","canonicalTextSha256":"f2ef11e858c11340a1d069dd7301e7a03b3358c273cf91681d80970717fb6b1c"},"sources/Python/converted/2.Python_Data_Struct/notebook.md":{"sourceSha256":"b22b730af709e02d0009f11919302963e3efaa6c020949866f1e86d6f47e25fc","canonicalTextSha256":"b22b730af709e02d0009f11919302963e3efaa6c020949866f1e86d6f47e25fc"},"sources/Python/converted/3.numpy/notebook.md":{"sourceSha256":"f2bccd1d5c7492037ac66a7c4de1b34220d0b8812f4773a0978eca434b5bcfa9","canonicalTextSha256":"f2bccd1d5c7492037ac66a7c4de1b34220d0b8812f4773a0978eca434b5bcfa9"},"sources/Python/converted/4.PyPlot/notebook.md":{"sourceSha256":"8f0bf07a3cf8561f8fccfce4736fa515597960640d561e98ada980abcb68cd18","canonicalTextSha256":"8f0bf07a3cf8561f8fccfce4736fa515597960640d561e98ada980abcb68cd18"}}} -->
