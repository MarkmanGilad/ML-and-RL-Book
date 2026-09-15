<!-- editorlm-hebrew-html-start -->
<style>
html, body, .vscode-body, .markdown-body, .markdown-preview {
  direction: rtl !important; text-align: right !important;
}
.book { box-sizing: border-box; max-width: 960px; margin: auto; padding: 24px;
  background: #ffffff; color: #183b50; font-family: Arial, sans-serif; line-height: 1.8; }
.book p, .book ul, .book ol, .book li, .book h1, .book h2, .book h3, .book th, .book td,
.book figcaption, .book .step, .book .about-card, .book .note {
  direction: rtl !important; text-align: right !important; unicode-bidi: isolate;
}
.book a { color: #176f78; text-underline-offset: 4px; }
.book a:focus-visible { outline: 3px solid #239b91; outline-offset: 4px; }
.book ul { padding-right: 24px; padding-left: 0; }
.book li { margin: 7px 0; }
.book h1 { font-size: 32px; border: 0; margin: 40px 0 20px; }
.book h3 { font-size: 23px; color: #174e49; border: 0; border-right: 4px solid #299c91;
  padding: 8px 16px; margin: 32px 0 16px; background: #eff7f5; border-radius: 5px; }
.book .cover { position: relative; overflow: hidden; padding: 52px 48px 44px; margin: 0 0 28px;
  border-radius: 18px; color: #ffffff;
  background: linear-gradient(135deg, #0c2236 0%, #123a55 48%, #145f66 100%);
  box-shadow: 0 12px 34px rgba(12, 34, 54, .28); }
.book .cover::before { content: ""; position: absolute; width: 420px; height: 420px; border-radius: 50%;
  left: -140px; top: -190px; background: radial-gradient(circle, rgba(56,189,176,.42), rgba(56,189,176,0) 70%); }
.book .cover::after { content: ""; position: absolute; width: 360px; height: 360px; border-radius: 50%;
  right: -120px; bottom: -200px; background: radial-gradient(circle, rgba(145,225,214,.28), rgba(145,225,214,0) 70%); }
.book .cover > * { position: relative; z-index: 1; }
.book .cover .eyebrow { display: inline-block; color: #91e1d6; font-size: 14px; letter-spacing: 3px;
  padding: 6px 14px; border: 1px solid rgba(145,225,214,.45); border-radius: 999px; }
.book .cover h1 { color: #ffffff; font-size: 52px; line-height: 1.2; margin: 26px 0 10px; letter-spacing: -.5px; }
.book .cover .subtitle { color: #b8ece4; font-size: 27px; font-weight: bold; }
.book .cover .rule { width: 120px; height: 5px; margin: 22px 0 0; border-radius: 3px;
  background: linear-gradient(90deg, #38bdb0, #91e1d6); }
.book .cover .author { font-size: 24px; margin-top: 26px; }
.book .cover .audience { color: #bcd4df; font-size: 15px; margin-top: 4px; }
.book .cover .badges { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px; }
.book .cover .badges span { padding: 7px 15px; border-radius: 999px; font-size: 14px; font-weight: bold;
  background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.22); color: #eaf7f5; }
.book .cover .badges span.accent { background: #38bdb0; border-color: #38bdb0; color: #0c2236; }
.book .lead { font-size: 19px; line-height: 1.9; color: #12303f; }
.book .path { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 22px 0 8px; }
.book .step { padding: 16px 16px 14px; border-radius: 12px; background: #f4f8fb; border: 1px solid #d4e3e9;
  border-top: 5px solid #299c91; }
.book .step .num { display: inline-flex; align-items: center; justify-content: center; width: 34px; height: 34px;
  border-radius: 50%; background: #174e49; color: #fff; font-weight: bold; font-size: 17px; margin-bottom: 8px; }
.book .step strong { display: block; font-size: 19px; color: #153b56; margin-bottom: 4px; }
.book .step span { display: block; font-size: 14.5px; color: #496576; line-height: 1.6; }
.book .step.s2 { border-top-color: #3776ab; } .book .step.s2 .num { background: #3776ab; }
.book .step.s3 { border-top-color: #b45309; } .book .step.s3 .num { background: #b45309; }
.book .step.s4 { border-top-color: #7c3aed; } .book .step.s4 .num { background: #7c3aed; }
.book .gallery { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin: 24px 0 8px; }
.book .gallery figure { margin: 0; padding: 14px; border-radius: 12px; background: #f7fafc; border: 1px solid #d4e3e9;
  display: flex; flex-direction: column; }
.book .gallery .frame { display: flex; align-items: center; justify-content: center; height: 190px;
  background: #ffffff; border-radius: 8px; overflow: hidden; }
.book .gallery img { max-width: 100%; max-height: 100%; width: auto; height: auto; display: block; }
.book .gallery figcaption { font-size: 14.5px; color: #3f5a6a; margin-top: 10px; line-height: 1.6; }
.book .gallery figcaption strong { color: #153b56; }
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
.book .note.warm { background: #fff7d6; color: #423611; border-right-color: #ffd343; font-size: 16px; padding: 16px 20px; }
.book .note.warm strong { font-size: 18px; }
.book code { direction: ltr; unicode-bidi: isolate; }
@media (max-width: 760px) {
  .book .path { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .book .gallery { grid-template-columns: 1fr; }
}
@media (max-width: 600px) {
  .book { padding: 12px; }
  .book .cover { padding: 32px 24px 28px; }
  .book .cover h1 { font-size: 36px; }
  .book .cover .subtitle { font-size: 21px; }
  .book .path { grid-template-columns: 1fr; }
  .book .course-grid { grid-template-columns: 1fr; }
}
@media print {
  .book { max-width: none; padding: 0; }
  .book .cover { break-after: page; box-shadow: none; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .book .book-nav { display: none; }
  .book .course-card, .book .resource-box, .book .step, .book .gallery figure { break-inside: avoid; }
  .book h1, .book h3 { break-after: avoid; }
}
</style>
<!-- editorlm-hebrew-html-end -->

<div class="book" dir="rtl" lang="he">

<div class="cover">
<div class="eyebrow">לחשוב · לתכנת · ללמוד</div>
<h1>למידת מכונה ולמידת חיזוק</h1>
<div class="subtitle">באמצעות בניית משחקים</div>
<div class="rule"></div>
<div class="author">גלעד מרקמן</div>
<div class="audience">לתלמידי כיתות י״א–י״ב במגמת הנדסת תוכנה, במסלול למידת מכונה ולמידת חיזוק</div>
<div class="badges">
<span class="accent">5 יחידות לימוד</span>
<span>מגמת הנדסת תוכנה</span>
<span>תוכנית מוכרת על ידי משרד החינוך</span>
<span>Python · Pygame · PyTorch</span>
</div>
</div>

<nav class="book-nav" aria-label="ניווט בספר">
<a class="toc-link" href="#book-toc">תוכן העניינים</a>
<a href="#about">על הספר</a>
<a href="#course-materials">אתר הקורס וחומרי ליווי</a>
<a href="01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/01-%D7%9E%D7%91%D7%95%D7%90.md">מתחילים לקרוא ←</a>
</nav>

<a id="about"></a>

### על הספר

<p class="lead">איך מלמדים מחשב לזהות ספרה בכתב יד, לנחש גובה של אדם לפי גובה הוריו, או לנצח במשחק איקס־עיגול בלי שמישהו כתב לו את חוקי הניצחון? זהו הנושא של הספר: <strong>למידת מכונה</strong> ו<strong>למידת חיזוק</strong>, שני התחומים שבליבה של הבינה המלאכותית של ימינו. את שניהם לומדים כאן דרך <strong>בניית משחקים</strong>: כותבים משחק, מגדירים לו חוקים ומטרה, ואז מלמדים תוכנה לשחק בו ולהשתפר מתוך התנסות.</p>

**למידת מכונה** היא הדרך לגרום למחשב ללמוד מדוגמאות במקום מהוראות מפורשות. במקום לכתוב כלל לכל מקרה, מראים למודל דוגמאות רבות עם התשובה הנכונה, והוא לומד לנחש, למדוד את הטעות שלו ולתקן את עצמו שוב ושוב עד שהוא מדייק. מכאן מגיעים ל**רשתות נוירונים**: בונים אותן צעד אחר צעד עם PyTorch, החל בנוירון יחיד ורגרסיה פשוטה ועד רשתות עמוקות ורשתות קונבולוציה, ומאמנים אותן לזהות ספרות, פריטי לבוש ותמונות של חתולים.

**למידת חיזוק** עוסקת בשאלה אחרת: איך לומדים לפעול נכון כשאין מי שיאמר לנו מהי התשובה הנכונה בכל מצב? בדיוק כמו כלב שלומד פקודה חדשה מתוך חטיפים, **סוכן** תוכנה מנסה מהלכים במשחק, מקבל **תגמול** על תוצאות טובות, ולומד בהדרגה מדיניות מנצחת. מתחילים במבוכים ובפאזלים שחוקיהם ידועים, ממשיכים ללמידה מתוך ניסיון בלבד, ובסוף המסלול משלבים את שני התחומים: רשת נוירונים משמשת „מוח” לסוכן, והוא מאמן את עצמו לנצח באיקס־עיגול ובמשחקים נוספים.

<div class="gallery">
<figure>
<div class="frame"><img src="assets/slides/d7f4427fe8/image11.png" alt="רשת נוירונים קטנה: שני קלטים, שכבת ביניים ופלט אחד"></div>
<figcaption><strong>רשת נוירונים.</strong> קלטים, משקלים ופונקציות אקטיבציה. בחלק ג בונים רשתות כאלה ומאמנים אותן על נתונים ותמונות.</figcaption>
</figure>
<figure>
<div class="frame"><img src="assets/slides/d7f4427fe8/image14.jpg" alt="כלב כסוכן ואישה כסביבה: פעולות, תגמולים ותצפיות"></div>
<figcaption><strong>למידת חיזוק.</strong> כמו באימון כלב: הסוכן פועל, הסביבה מחזירה תגמול ותצפית, וכך נלמדת ההתנהגות הרצויה.</figcaption>
</figure>
<figure>
<div class="frame"><img src="assets/rl/maze/maze-solved.png" alt="מבוך 5×5 שבו הסוכן מצא את המסלול אל היעד"></div>
<figcaption><strong>לומדים דרך משחקים.</strong> מבוכים, פאזלים ואיקס־עיגול הם המגרש שבו הסוכן מתאמן, וכל אלגוריתם נבחן במשחק אמיתי.</figcaption>
</figure>
</div>

הספר מלווה את תוכנית הלימודים **„בינה מלאכותית ולמידת מכונה באמצעות פיתוח משחקים”** במגמת הנדסת תוכנה, תוכנית בהיקף **5 יחידות לימוד** המוכרת על ידי משרד החינוך ונלמדת בכיתות י״א–י״ב. סדר הפרקים עוקב אחר סדר הנושאים בתוכנית, וכל פרק מחבר בין ההסבר, האלגוריתם והקוד.

### מסלול הלימוד

לומדים בארבעה חלקים, וכל חלק נשען על קודמו:

<div class="path">
<div class="step s1"><span class="num">א</span><strong>פייתון</strong><span>שפת פייתון והספריות שישמשו אותנו בהמשך: NumPy, PyPlot ו־Pandas.</span></div>
<div class="step s2"><span class="num">ב</span><strong>pygame</strong><span>בניית משחק גרפי: לולאה ראשית, ציור, אירועים, אנימציה, ספרייטים והתנגשויות.</span></div>
<div class="step s3"><span class="num">ג</span><strong>למידת מכונה</strong><span>מנגזרות ו־Gradient Descent דרך רגרסיה ועד רשתות נוירונים ו־CNN עם PyTorch.</span></div>
<div class="step s4"><span class="num">ד</span><strong>למידת חיזוק</strong><span>סוכן וסביבה, MDP, תכנון דינמי, מונטה קרלו, TD ולמידת חיזוק עמוקה: DQN ו־DDQN.</span></div>
</div>

<p class="note warm"><strong>הספר אינו קורס תכנות.</strong> הוא יוצא מנקודת הנחה שהתלמידים כבר למדו את יסודות התכנות: משתנים, תנאים, לולאות, פונקציות ומחלקות, בשפה אחרת. חלק א מלמד את <strong>שפת פייתון</strong> ואת הספריות הדרושות בהמשך, ולא את מושגי היסוד של התכנות עצמם.</p>

<a id="course-materials"></a>

### אתר הקורס וחומרי ליווי

הקורס זמין גם באתר **„תכנות באינטרנט” של גלעד מרקמן**, וכולל סרטונים, מצגות ודוגמאות קוד. הקישורים הבאים מובילים למדורי הקורס ולחומרי הליווי המתאימים לכל חלק בספר.

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
- [א.13 — פונקציות מתקדמות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/13-%D7%A4%D7%95%D7%A0%D7%A7%D7%A6%D7%99%D7%95%D7%AA%20%D7%9E%D7%AA%D7%A7%D7%93%D7%9E%D7%95%D7%AA.md)
- [א.14 — חריגות — טיפול בשגיאות בזמן ריצה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/14-%D7%97%D7%A8%D7%99%D7%92%D7%95%D7%AA.md)
- [א.15 — רקורסיה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/15-%D7%A8%D7%A7%D7%95%D7%A8%D7%A1%D7%99%D7%94.md)
- [א.16 — חיפוש, מיון ויעילות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/16-%D7%97%D7%99%D7%A4%D7%95%D7%A9%20%D7%95%D7%9E%D7%99%D7%95%D7%9F.md)
- [א.17 — טבלאות גיבוב](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/17-%D7%92%D7%99%D7%91%D7%95%D7%91.md)
- [א.18 — מחלקות](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/18-%D7%9E%D7%97%D7%9C%D7%A7%D7%95%D7%AA.md)
- [א.19 — ירושה והכלה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/19-%D7%99%D7%A8%D7%95%D7%A9%D7%94.md)
- [א.20 — קבצים — קריאה וכתיבה](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/20-%D7%A7%D7%91%D7%A6%D7%99%D7%9D.md)
- [א.21 — NumPy — מערכים וחישובים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/21-NumPy.md)
- [א.22 — PyPlot — גרפים ותרשימים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/22-PyPlot.md)
- [א.23 — תמונות כמערכים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/23-%D7%AA%D7%9E%D7%95%D7%A0%D7%95%D7%AA%20%D7%9B%D7%9E%D7%A2%D7%A8%D7%9B%D7%99%D7%9D.md)
- [א.24 — Pandas — טבלאות וניתוח נתונים](01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/24-Pandas.md)

### חלק ב — pygame

- [ב.1 — מעבר מ־Colab לעבודה מקומית](02-pygame/01-%D7%94%D7%AA%D7%A7%D7%A0%D7%94%20%D7%9E%D7%A7%D7%95%D7%9E%D7%99%D7%AA.md)
- [ב.2 — מבנה הלולאה הראשית](02-pygame/02-%D7%94%D7%9C%D7%95%D7%9C%D7%90%D7%94%20%D7%94%D7%A8%D7%90%D7%A9%D7%99%D7%AA.md)
- [ב.3 — אירועים וסגירת החלון](02-pygame/03-%D7%90%D7%99%D7%A8%D7%95%D7%A2%D7%99%D7%9D%20%D7%95%D7%A1%D7%92%D7%99%D7%A8%D7%94.md)
- [ב.4 — משטחים, שכבות וצבעים](02-pygame/04-%D7%9E%D7%A9%D7%98%D7%97%D7%99%D7%9D%20%D7%95%D7%A6%D7%91%D7%A2%D7%99%D7%9D.md)
- [ב.5 — ציור צורות גאומטריות](02-pygame/05-%D7%A6%D7%95%D7%A8%D7%95%D7%AA%20%D7%92%D7%90%D7%95%D7%9E%D7%98%D7%A8%D7%99%D7%95%D7%AA.md)
- [ב.6 — טעינה והצגה של תמונות](02-pygame/06-%D7%AA%D7%9E%D7%95%D7%A0%D7%95%D7%AA.md)
- [ב.7 — אינטראקציה עם המשתמש: עכבר ומקלדת](02-pygame/07-%D7%9E%D7%A7%D7%9C%D7%93%D7%AA%20%D7%95%D7%A2%D7%9B%D7%91%D7%A8.md)
- [ב.8 — שעון, קצב פריימים ורענון המסך](02-pygame/08-%D7%A9%D7%A2%D7%95%D7%9F%20%D7%95%D7%A8%D7%A2%D7%A0%D7%95%D7%9F.md)
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
- [ג.7 — רגרסיה לינארית — נקודה אחת](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/07-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99%D7%AA.md)
- [ג.8 — רגרסיה לינארית — כמה נקודות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/08-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%A2%D7%9D%20%D7%9B%D7%9E%D7%94%20%D7%A0%D7%A7%D7%95%D7%93%D7%95%D7%AA.md)
- [ג.9 — המחלקה nn.Linear](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/09-%D7%94%D7%9E%D7%97%D7%9C%D7%A7%D7%94%20nn.Linear.md)
- [ג.10 — רגרסיה לינארית וחשיבות נרמול הנתונים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/10-%D7%A0%D7%A8%D7%9E%D7%95%D7%9C%20%D7%A0%D7%AA%D7%95%D7%A0%D7%99%D7%9D.md)
- [ג.11 — רגרסיה לינארית במספר משתנים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/11-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%91%D7%9E%D7%A1%D7%A4%D7%A8%20%D7%9E%D7%A9%D7%AA%D7%A0%D7%99%D7%9D.md)
- [ג.12 — רגרסיה במספר משתנים — דוגמה](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/12-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%91%D7%9E%D7%A1%D7%A4%D7%A8%20%D7%9E%D7%A9%D7%AA%D7%A0%D7%99%D7%9D%20-%20%D7%93%D7%95%D7%92%D7%9E%D7%94.md)
- [ג.13 — רגרסיה לוגיסטית](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/13-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%95%D7%92%D7%99%D7%A1%D7%98%D7%99%D7%AA.md)
- [ג.14 — רגרסיה לוגיסטית — דוגמאות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/14-%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%95%D7%92%D7%99%D7%A1%D7%98%D7%99%D7%AA%20-%20%D7%93%D7%95%D7%92%D7%9E%D7%90%D7%95%D7%AA.md)
- [ג.15 — רשת נוירונים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/15-%D7%A8%D7%A9%D7%AA%20%D7%A0%D7%95%D7%99%D7%A8%D7%95%D7%A0%D7%99%D7%9D.md)
- [ג.16 — רשת נוירונים — דוגמאות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/16-%D7%A8%D7%A9%D7%AA%20%D7%A0%D7%95%D7%99%D7%A8%D7%95%D7%A0%D7%99%D7%9D%20-%20%D7%93%D7%95%D7%92%D7%9E%D7%90%D7%95%D7%AA.md)
- [ג.17 — רשת באמצעות מחלקה וסיווג](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/17-%D7%A8%D7%A9%D7%AA%20%D7%91%D7%90%D7%9E%D7%A6%D7%A2%D7%95%D7%AA%20%D7%9E%D7%97%D7%9C%D7%A7%D7%94%20%D7%95%D7%A1%D7%99%D7%95%D7%95%D7%92.md)
- [ג.18 — רשת באמצעות מחלקה וסיווג — דוגמאות](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/18-%D7%A8%D7%A9%D7%AA%20%D7%91%D7%90%D7%9E%D7%A6%D7%A2%D7%95%D7%AA%20%D7%9E%D7%97%D7%9C%D7%A7%D7%94%20%D7%95%D7%A1%D7%99%D7%95%D7%95%D7%92%20-%20%D7%93%D7%95%D7%92%D7%9E%D7%90%D7%95%D7%AA.md)
- [ג.19 — שמירה וטעינה של מודלים](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/19-%D7%A9%D7%9E%D7%99%D7%A8%D7%94%20%D7%95%D7%98%D7%A2%D7%99%D7%A0%D7%94.md)
- [ג.20 — רשתות קונבולוציה — CNN ו־CIFAR-10](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/20-%D7%A8%D7%A9%D7%AA%D7%95%D7%AA%20%D7%A7%D7%95%D7%A0%D7%91%D7%95%D7%9C%D7%95%D7%A6%D7%99%D7%94.md)
- [ג.21 — חתול או לא חתול — CNN לסיווג בינארי](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/21-%D7%97%D7%AA%D7%95%D7%9C%20%D7%90%D7%95%20%D7%9C%D7%90%20%D7%97%D7%AA%D7%95%D7%9C.md)
- [ג.22 — מעקב והשוואת ניסויים עם <span dir="ltr">W&amp;B</span>](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/22-WandB.md)
- [ג.23 — השלמות — מגבלות הקו הישר ורגרסיה באמצעות רשת](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/23-%D7%94%D7%A9%D7%9C%D7%9E%D7%95%D7%AA%20-%20%D7%A8%D7%92%D7%A8%D7%A1%D7%99%D7%94%20%D7%9C%D7%90%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99%D7%AA.md)
- [ג.24 — השלמות — Moon — ללמוד גבול סיווג שאינו ישר](03-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%9E%D7%9B%D7%95%D7%A0%D7%94/24-%D7%94%D7%A9%D7%9C%D7%9E%D7%95%D7%AA%20-%20Moon%20%D7%A1%D7%99%D7%95%D7%95%D7%92%20%D7%9C%D7%90%20%D7%9C%D7%99%D7%A0%D7%90%D7%A8%D7%99.md)

### חלק ד — למידת חיזוק

- [ד.1 — מבוא ללמידת חיזוק](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/01-%D7%9E%D7%91%D7%95%D7%90.md)
- [ד.2 — התקנת PyTorch במחשב האישי](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/02-%D7%94%D7%AA%D7%A7%D7%A0%D7%AA%20PyTorch%20%D7%91%D7%9E%D7%97%D7%A9%D7%91.md)
- [ד.3 — מודל סביבה–סוכן ו־MDP](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/03-%D7%9E%D7%95%D7%93%D7%9C%20%D7%A1%D7%91%D7%99%D7%91%D7%94%20%D7%A1%D7%95%D7%9B%D7%9F%20%D7%95-MDP.md)
- [ד.4 — תכנון דינמי: Policy Iteration](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/04-Policy%20Iteration.md)
- [ד.5 — תכנון דינמי: Value Iteration](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/05-Value%20Iteration.md)
- [ד.6 — Value Iteration — פאזל 8](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/06-Value%20Iteration%20-%20puzzle%208.md)
- [ד.7 — מונטה קרלו — למידה מהתנסות](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/07-%D7%9E%D7%95%D7%A0%D7%98%D7%94%20%D7%A7%D7%A8%D7%9C%D7%95.md)
- [ד.8 — מונטה קרלו באיקס עיגול — טבלת Q וקוד האימון](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/08-%D7%9E%D7%95%D7%A0%D7%98%D7%94%20%D7%A7%D7%A8%D7%9C%D7%95%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md)
- [ד.9 — <span dir="ltr" style="unicode-bidi:isolate">Temporal Difference</span>](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/09-Temporal%20Difference.md)
- [ד.10 — TD באיקס עיגול ו־AfterState](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/10-TD%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md)
- [ד.11 — למידת חיזוק עמוקה](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/11-DQN.md)
- [ד.12 — בנייה ואימון של DQN באיקס עיגול](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/12-DQN%20%D7%91%D7%90%D7%99%D7%A7%D7%A1%20%D7%A2%D7%99%D7%92%D7%95%D7%9C.md)
- [ד.13 — DDQN — ההבדל מ־DQN](04-%D7%9C%D7%9E%D7%99%D7%93%D7%AA%20%D7%97%D7%99%D7%96%D7%95%D7%A7/13-DDQN.md)

<nav class="book-nav" aria-label="ניווט בספר">
<a class="toc-link" href="#book-toc">תוכן העניינים</a>
<a href="#course-materials">אתר הקורס וחומרי ליווי</a>
<a href="01-%D7%A4%D7%99%D7%99%D7%AA%D7%95%D7%9F/01-%D7%9E%D7%91%D7%95%D7%90.md">מתחילים לקרוא ←</a>
</nav>

</div>

<!-- editorlm-source-versions: {"schemaVersion":1,"sources":{"sources/Python/Python_Intro_Colab.pptx":{"sourceSha256":"6661ef452ccbf6f70f9e9d413207d0f16914ac4da9a38026e817f7e8d932658c","canonicalTextSha256":"2cca9ddeeb2f1c940efaadd82221ebda54fb08e2814fd46db348a62cdc164917"},"sources/Python/Python_Basic.pptx":{"sourceSha256":"32a2d56f6cb0e1eacf4a8a28f14d7932648610f4248f7178dae91b80b6ef7e84","canonicalTextSha256":"0a301b7608d0440e9cfaab4e39bd7bbb9518eaf76710de862723aa719cc60e4a"},"sources/Python/converted/1.Python_Basic/notebook.md":{"sourceSha256":"2d605efefadda4ead3844d4ae7e8066d8443ea6927868f6b4ca26a4bdc66d16c","canonicalTextSha256":"2d605efefadda4ead3844d4ae7e8066d8443ea6927868f6b4ca26a4bdc66d16c"},"sources/Python/Python_Classes_Inheritance.pptx":{"sourceSha256":"ad085713a21c8b50a6210c1b43f31e3421aad37238c20ec5a6c78825cf178af4","canonicalTextSha256":"09ec2e29ca4c246d64556136e69fee1eeac8a6234f55b06dac6d77cecd09e7e5"},"sources/Python/Python_Data_Strucrures.pptx":{"sourceSha256":"af0d66fc064d82bd80d368b0e9d39716f653abe73240936a8fce03b3ad2ff283","canonicalTextSha256":"80dd4b6c86b82109570ee1c3b0062963aab08de123e173c90e0967af586bfee4"},"sources/Python/Python_Numpy.pptx":{"sourceSha256":"d1a86b84fd49ca2baee3a81586a78246cf31d582742844b229c2f8f576d52fa3","canonicalTextSha256":"fe990439bdef892516fa8983a16f5eed04168924c84b6e9d819b5a94be5ca314"},"sources/Python/Python_PyPlot.pptx":{"sourceSha256":"01cadb34d9c969eeb2e63490275e6f56122c7ce9f3d9f193296e1e796656d85b","canonicalTextSha256":"f2ef11e858c11340a1d069dd7301e7a03b3358c273cf91681d80970717fb6b1c"},"sources/Python/converted/2.Python_Data_Struct/notebook.md":{"sourceSha256":"b22b730af709e02d0009f11919302963e3efaa6c020949866f1e86d6f47e25fc","canonicalTextSha256":"b22b730af709e02d0009f11919302963e3efaa6c020949866f1e86d6f47e25fc"},"sources/Python/converted/3.numpy/notebook.md":{"sourceSha256":"f2bccd1d5c7492037ac66a7c4de1b34220d0b8812f4773a0978eca434b5bcfa9","canonicalTextSha256":"f2bccd1d5c7492037ac66a7c4de1b34220d0b8812f4773a0978eca434b5bcfa9"},"sources/Python/converted/4.PyPlot/notebook.md":{"sourceSha256":"8f0bf07a3cf8561f8fccfce4736fa515597960640d561e98ada980abcb68cd18","canonicalTextSha256":"8f0bf07a3cf8561f8fccfce4736fa515597960640d561e98ada980abcb68cd18"}}} -->
