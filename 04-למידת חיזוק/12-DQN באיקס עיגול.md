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
<a href="11-DQN.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="13-DDQN.md">הבא ←</a>
</nav>

## ד.12 — בנייה ואימון של DQN באיקס עיגול

**המצגת:** [DQN באיקס עיגול](../../../sources/RL/7.DQN_tic_tac_toe.pptx) · **קוד:** [ReplayBuffer](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_replay.py) · [הרשת](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_model.py) · [הסוכן](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_agent.py) · [המאמן](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_train.py) · [הבודק](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_test.py) · [כל קובצי הקוד בגיטהב](https://github.com/MarkmanGilad/book/tree/main/assets/rl/code)

בפרק הקודם הכרנו את DQN כרעיון: רשת נוירונים במקום טבלת Q, מאגר מעברים שממנו דוגמים אצוות, ורשת מטרה שמייצבת את היעדים. בפרק הזה נהפוך את הרעיון לקוד עובד. השאלה המעשית היא איך כל אחד מהרכיבים נראה ב־PyTorch, ואיך מחברים אותם ללולאת אימון אחת בלי לערבב בין המשחק החי לבין הדגימות מהמאגר.

ניישם את DQN על איקס עיגול: הסוכן X ישחק מול יריב אקראי, ישמור את המעברים שחווה ויאמן רשת שמעריכה את כדאיות המהלכים. המשחק כבר מוכן. עיקר העבודה כאן הוא לחבר את מאגר הדגימות, הרשת, הסוכן ולולאת האימון למערכת אחת.

כדאי לשים לב כמה מהמבנה כבר מוכר. לולאת המשחק ופונקציית הדגימה `sample_step` הן אותן פונקציות מהפרקים הטבלאיים; מחלקת הרשת, האופטימייזר, פונקציית ההפסד וצמד הקריאות `backward` ו־`step` הם בדיוק מה שלמדנו בחלק ג. החדש הוא רק החיבור: הנתונים לאימון מגיעים מהמשחק, והיעדים מחושבים לפי נוסחת DQN.

נשתמש ב־[DQN רגיל](11-DQN.md#dqn-target): רשת המטרה תבחר ותעריך את פעולת ההמשך שביעד. כאן נוכל לזהות במימוש בדיוק היכן מחשבים את המקסימום.

### הממשק שהאימון מקבל מהמשחק

נשתמש באותו [ממשק איקס עיגול](08-מונטה%20קרלו%20באיקס%20עיגול.md#game-interface). המצב שומר לוח ותור, והפעולה היא `(row, col)`. הפונקציה [sample_step](08-מונטה%20קרלו%20באיקס%20עיגול.md#sample-step) מבצעת את פעולת X ואת תגובת היריב, אם נדרשת, ומחזירה `(next_state, reward, done)`.

איך מגישים לוח לרשת נוירונים? הרשת מקבלת מספרים בלבד, ולכן נציג את הלוח כרשימה של תשעה מספרים, אחד לכל תא (1 ל־X, ‏−1 ל־O ו־0 לתא ריק, כפי ש־`State.board` כבר מיוצג בממשק). הרשת תקבל את תשעת תאי הלוח בלבד. זה מספיק לדוגמה הזאת משום שכל מצב החלטה שנאמן עליו הוא של X; התגמול תמיד מנקודת מבטו. אם מאמנים בהמשך סוכן לשני התורים, צריך להתאים גם את הייצוג ואת משמעות הערכים.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L1-L15] -->

### ReplayBuffer — שומרים חמישה שדות ודוגמים אצווה

הרכיב הראשון שנבנה הוא הזיכרון של הסוכן. תפקידו פשוט: לקלוט מעבר אחד בכל פעם, ולהחזיר אצווה אקראית של מעברים כשמבקשים. נממש את [מאגר המעברים](11-DQN.md#replay) באמצעות `deque`, תור דו־כיווני מהספרייה הסטנדרטית. הפרמטר `maxlen` מגביל אותו ל־10,000 רשומות; כשהוא מלא והכנסנו רשומה חדשה, הישנה ביותר תצא אוטומטית. כך המאגר מכיל תמיד את ההתנסות האחרונה, ומעברים מתקופת האימון המוקדמת, שבה הסוכן שיחק גרוע, נשכחים בהדרגה.

כל מעבר יישמר כחמישה טנסורים. נזכיר מחלק ג שטנסור הוא המערך הרב־ממדי של PyTorch, ושרשת מצפה לקלט בצורת אצווה: ממד ראשון למספר הדוגמאות ואחריו ממדי הדוגמה עצמה. חשוב לשמור גם את הפעולה, משום שהרשת שלנו מקבלת מצב **ופעולה** כדי לחשב Q. כל טנסור של דוגמה אחת כולל ממד אצווה של 1, כך שאפשר לחבר דוגמאות בעזרת `vstack`.

<div class="code-panel" dir="ltr">

```python
from collections import deque
import random
import torch

class ReplayBuffer:
    def __init__(self, capacity=10000, seed=2):
        self.buffer = deque(maxlen=capacity)
        self.rng = random.Random(seed)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((
            torch.tensor(state.board, dtype=torch.float32).reshape(1, 9),
            torch.tensor(action, dtype=torch.float32).reshape(1, 2),
            torch.tensor([[reward]], dtype=torch.float32),
            torch.tensor(next_state.board, dtype=torch.float32).reshape(1, 9),
            torch.tensor([[done]], dtype=torch.bool)))

    def sample(self, batch_size):
        batch = self.rng.sample(list(self.buffer), batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return (torch.vstack(states), torch.vstack(actions),
                torch.vstack(rewards), torch.vstack(next_states),
                torch.vstack(dones))

    def __len__(self):
        return len(self.buffer)
```

</div>

המתודה `push` ממירה כל שדה לטנסור כבר בזמן השמירה, כך שבזמן הדגימה לא נצטרך המרות. `sample` בוחרת `batch_size` רשומות אקראיות מהמאגר. `zip(*batch)` מפרידה את רשומות האצווה לפי שדות: כל המצבים יחד, כל הפעולות יחד וכן הלאה. `vstack` מערים את הטנסורים של הדוגמאות זה על זה לטנסור אחד. לאחר האיחוד, עבור אצווה בגודל B יתקבלו הצורות הבאות:

| טנסור | צורה | תוכן |
| --- | --- | --- |
| `states` | B×9 | לוחות לפני פעולות X |
| `actions` | B×2 | קואורדינטות הפעולות |
| `rewards` | B×1 | תגמולים מנקודת מבט X |
| `next_states` | B×9 | לוחות אחרי צעד הלמידה |
| `dones` | B×1 | האם כל מעבר הסתיים |

המאמן יקרא ל־`sample` רק כאשר יש לפחות B רשומות. לכן אין צורך לצמצם בשקט את גודל האצווה, ואין ניסיון לפרק מאגר ריק. קלט הרשת והתגמולים הם `float32`; דגלי הסיום הם בוליאניים.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L17-L33] -->

### רשת DQN — מצב ופעולה נכנסים, Q יוצא

הרכיב השני הוא הרשת עצמה, שמחליפה את טבלת Q. היא מקבלת מצב ופעולה ומחזירה מספר אחד: אומדן ל־Q של אותו זוג. תשעת תאי הלוח ושתי קואורדינטות הפעולה יוצרים קלט בן 11 מספרים. נשתמש בשתי שכבות חבויות של 128 ו־64 יחידות, ובפלט יחיד:

<div class="math-panel" dir="ltr">

$$
11 \to 128 \to 64 \to 1
$$

</div>

זהו אותו מבנה של רשת Fully Connected שבנינו בחלק ג, רק עם קלט ופלט אחרים. אחרי כל שכבה חבויה נפעיל ReLU, פונקציית האקטיבציה שמאפסת ערכים שליליים ומאפשרת לרשת ללמוד קשרים לא לינאריים. בשכבת הפלט לא נוסיף אקטיבציה: ערך Q אינו הסתברות, ויכול להיות שלילי, למשל כשהמהלך מוביל להפסד. כל הרשת והטנסורים בדוגמה נמצאים על CPU.

<div class="code-panel" dir="ltr">

```python
import torch
from torch import nn

class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(11, 128)
        self.linear2 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)

    def forward(self, states, actions):
        x = torch.cat((states, actions), dim=1)
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        return self.output(x)
```

</div>

חיבור הטנסורים מתבצע לאורך ממד העמודות: B×9 ו־B×2 הופכים ל־B×11. הפלט הוא B×1. נכתוב `Q(states, actions)` כדי להפעיל את הרשת דרך המעטפת של `nn.Module`; החיבור הוגדר ב־`forward`, ואין צורך להחליף את `__call__`.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L35-L41] -->

### DQNAgent — פעולה חוקרת או חמדנית

הרכיב השלישי הוא הסוכן: מי שמקבל מצב ומחזיר פעולה. בסוכן הטבלאי הבחירה החמדנית הייתה חיפוש בטבלה; כאן היא תהיה הרצת הרשת על כל פעולה חוקית. הסוכן מחזיק את הסביבה ואת הרשת הראשית. בזמן האימון הוא יכול לחקור; בזמן בדיקה הוא יבחר תמיד לפי תחזית הרשת. נשמור את הדגל בשם `training`, ואת המתודה לשינוי המצב בשם `set_training`, כדי שלא נסתיר מתודה באמצעות שדה בעל אותו שם.

<div class="code-panel" dir="ltr">

```python
class DQNAgent:
    def __init__(self, env, model, seed=0, training=True):
        self.env = env
        self.model = model
        self.rng = random.Random(seed)
        self.set_training(training)

    def set_training(self, enabled):
        self.training = enabled
        self.model.train(enabled)

    def get_action(self, state, epoch=0):
        actions = self.env.get_actions(state)
        if not actions:
            raise ValueError('No action in a terminal state')
        epsilon = epsilon_at(epoch, decay=5000) if self.training else 0.0
        if self.rng.random() < epsilon:
            return self.rng.choice(actions)
        states = torch.tensor(state.board, dtype=torch.float32)
        states = states.reshape(1, 9).repeat(len(actions), 1)
        action_tensor = torch.tensor(actions, dtype=torch.float32)
        with torch.no_grad():
            values = self.model(states, action_tensor).flatten()
        return actions[values.argmax().item()]
```

</div>

`epsilon_at` היא פונקציית הדעיכה המעריכית מ־[פרק מונטה קרלו](07-מונטה%20קרלו.md#epsilon-decay). כאן נשתמש ב־`decay=5000`, לפי קובץ הסוכן של DQN. בתחילת האימון ε=1 ובהמשך הוא מתקרב ל־0.01. בזמן בדיקה ε=0 בלי תלות במספר האפיזודה.

בבחירה החמדנית אנחנו משכפלים את אותו מצב לשורה לכל פעולה חוקית. למשל, אם יש ארבע משבצות פנויות, הרשת מקבלת ארבע שורות ומחזירה ארבעה ערכי Q. `argmax` נותנת את האינדקס של הערך הגדול ביותר, ובעזרתו מחזירים פעולה מתוך הרשימה החוקית המקורית.

`no_grad` מונע בניית גרף גרדיאנטים בזמן בחירת פעולה: כאן רק שואלים את הרשת, לא מאמנים אותה, ולכן אין טעם לשמור מידע לחישוב נגזרות. `train(False)` מעביר את הרשת למצב הערכה; הוא אינו תחליף ל־`no_grad`. שני המנגנונים משמשים למטרות שונות: הראשון חוסך חישוב וזיכרון של גרדיאנטים, והשני מסמן לרשת שהיא במצב בדיקה, מה שמשפיע על סוגי שכבות שמתנהגים אחרת באימון ובבדיקה. ברשת הפשוטה שלנו אין שכבות כאלה, אבל נכון להרגיל את עצמנו לקרוא לו.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L43-L49] -->

<a id="next-q-values"></a>

### ערכי ההמשך של אצווה

כדי לבנות את היעד y = R + γ·max Q(S′,a′;w⁻) לכל דוגמה באצווה, צריך את החלק "max Q(S′,a′;w⁻)": הערך הטוב ביותר שאפשר להשיג במצב הבא, לפי רשת המטרה. לפני לולאת האימון נכתוב פונקציה לחישוב ערכי ההמשך. כל שורה ב־`next_states` מתארת לוח אחר. במעבר סופי נשאיר 0; במעבר שאינו סופי נמצא את המשבצות הפנויות וניקח את הערך המרבי של **רשת המטרה** בלבד.

<div class="code-panel" dir="ltr">

```python
def next_q_values(target, next_states, dones):
    values = torch.zeros((len(next_states), 1), dtype=torch.float32)
    with torch.no_grad():
        for i, board in enumerate(next_states):
            if dones[i].item():
                continue
            actions = (board.reshape(3, 3) == 0).nonzero().float()
            states = board.reshape(1, 9).repeat(len(actions), 1)
            values[i, 0] = target(states, actions).max()
    return values
```

</div>

הביטוי `board.reshape(3, 3) == 0` יוצר לוח בוליאני שבו אמת מסמנת תא ריק, ו־`nonzero` מחזירה כאן את קואורדינטות התאים הריקים, כלומר את הפעולות החוקיות. איננו צריכים ליצור מחדש את כל אובייקט המשחק כדי לקבל אותן. אחר כך, כמו בסוכן, משכפלים את הלוח לשורה אחת לכל פעולה, ורשת המטרה מחזירה ערך לכל שורה. בדיקת `done` מקדימה את החיפוש, כך שלוח סופי אינו דורש פעולה מדומה או חישוב מקסימום על רשימה ריקה.

כאן המקסימום מחושב כולו ברשת המטרה. בפרק הבא נבחן את השינוי שמציע [DDQN](13-DDQN.md) לחישוב זה.

### הכנת המאמן ורשת המטרה

לפני האימון נקבע כמה ניסיון לאסוף, כיצד לדגום ממנו ובאיזה קצב לעדכן את הרשתות. נשתמש בפרמטרים הבאים:

<div class="code-panel" dir="ltr">

```python
EPOCHS = 30000
C = 1000
BATCH_SIZE = 64
LEARNING_RATE = 0.1
GAMMA = 0.99
```

</div>

`EPOCHS` הוא מספר המשחקים, `C` הוא מספר **האפיזודות שהסתיימו** בין סנכרוני המטרה, ו־`BATCH_SIZE` הוא מספר המעברים בכל עדכון. `LEARNING_RATE` הוא קצב הלמידה של האופטימייזר, ו־`GAMMA` הוא מקדם ההיוון; ערך 0.99 אומר שהסוכן כמעט אינו מקטין את משקלם של תגמולים רחוקים, וזה הגיוני במשחק שבו כל התגמול מגיע בסוף. נשתמש ב־SGD כדי לעדכן את הרשת הראשית. שימו לב שהמונח "אפוק" מקבל כאן משמעות שונה מזו שבחלק ג: לא מעבר על כל מערך הנתונים, אלא משחק אחד.

באתחול ניצור שני אובייקטים נפרדים ונעתיק את משקלי הראשית למטרה. השמה כגון `target = Q` לא הייתה יוצרת רשת עצמאית, אלא שם נוסף לאותו אובייקט, וכל עדכון של Q היה משנה גם את "המטרה". `state_dict` הוא מילון של כל המשקלים ברשת, ו־`load_state_dict` מעתיק אותם לרשת אחרת באותו מבנה. האופטימייזר יקבל רק את פרמטרי Q; רשת המטרה לא תלמד דרך גרדיאנטים.

<div class="code-panel" dir="ltr">

```python
Q = DQN()
target = DQN()
target.load_state_dict(Q.state_dict())
target.eval()
target.requires_grad_(False)
optimizer = torch.optim.SGD(Q.parameters(), lr=LEARNING_RATE)
loss_function = torch.nn.MSELoss()
```

</div>

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L51-L53] -->

### לולאת האימון המלאה

עכשיו כל הרכיבים מוכנים, ונחבר אותם ללולאה אחת לפי הפסאודו־קוד מסוף הפרק הקודם: בכל צעד של המשחק החי בוחרים פעולה, שומרים את המעבר, ואם המאגר מלא מספיק מאמנים על אצווה; בסוף כל C משחקים מסנכרנים את רשת המטרה. המאמן הבא כולל את האתחול ואת לולאת המשחקים. המחלקות והפונקציות שהוצגו נשמרות בקבצים המקושרים בראש הפרק; קובץ המאמן כולל את הייבואים הנדרשים.

<div class="code-panel" dir="ltr">

```python
def train(epochs=EPOCHS, seed=0):
    torch.manual_seed(seed)
    env = TicTacToe()
    Q = DQN()
    agent = DQNAgent(env, Q, seed=seed)
    target = DQN()
    target.load_state_dict(Q.state_dict())
    target.eval()
    target.requires_grad_(False)
    replay = ReplayBuffer(seed=seed + 2)
    opponent_rng = random.Random(seed + 1)
    optimizer = torch.optim.SGD(Q.parameters(), lr=LEARNING_RATE)
    loss_function = torch.nn.MSELoss()
    losses = []
    for epoch in range(epochs):
        state = State()
        while not env.end_of_game(state):
            action = agent.get_action(state, epoch)
            next_state, reward, done = sample_step(
                env, state, action, opponent_rng)
            replay.push(state, action, reward, next_state, done)
            if len(replay) >= BATCH_SIZE:
                states, actions, rewards, next_states, dones = replay.sample(BATCH_SIZE)
                predictions = Q(states, actions)
                future_values = next_q_values(target, next_states, dones)
                targets = rewards + GAMMA * future_values * (~dones).float()
                loss = loss_function(predictions, targets)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                losses.append(loss.item())
            state = next_state
        if (epoch + 1) % C == 0:
            target.load_state_dict(Q.state_dict())
    return env, agent, losses
```

</div>

בכל צעד הסוכן בוחר מתוך המצב החי, ואילו `states` ו־`next_states` הם אצוות של דגימות מהמאגר. ההפרדה בשמות מונעת החלפה בטעות בין המשחק הנוכחי לבין משחקים קודמים.

המסכה `(~dones).float()` היא 0 במעברים סופיים ו־1 באחרים. כך היעד במעבר סופי נשאר בדיוק התגמול. כל אחד מ־`predictions`, ‏`rewards`, ‏`future_values` ו־`targets` הוא B×1, ולכן השוואת ה־MSE נעשית בין איברים מתאימים באצווה.

שלוש השורות `zero_grad`, ‏`backward` ו־`step` הן צעד האימון המוכר מחלק ג. איפוס הגרדיאנטים מקדים את `backward`, ואחריו `step` משנה את משקלי Q. ערכי ההמשך חושבו ללא גרדיאנט, ולכן אין עדכון עקיף של רשת המטרה, וה־backpropagation זורם רק דרך `predictions`, בדיוק כפי שדרשנו בפרק הקודם. `losses` שומרת מספר אחד לכל עדכון, לצורך עיון במהלך האימון.

גם מעבר סופי נכנס למאגר ומגיע לשלב האימון לפני שהלולאה נעצרת. הסנכרון נמצא **מחוץ ללולאת הצעדים**, ולכן מתבצע פעם אחת לאחר כל C משחקים שהסתיימו. אין סנכרון חוזר בכל צעד של אותו משחק.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L55-L57] -->

### שמירה ו־Tester

האימון נמשך זמן, ואיננו רוצים לחזור עליו בכל פעם שרוצים לשחק נגד הסוכן. בסוכן הטבלאי היה אפשר לשמור את המילון; כאן כל מה שהסוכן למד נמצא במשקלי הרשת, ולכן די לשמור אותם. שמירה מאפשרת להפעיל את הסוכן לבדיקה בלי לחזור על האימון. בסיום האימון נשמור את משקלי הרשת הראשית. קובץ המאמן עושה זאת ל־`dqn_weights.pth` בתיקיית הקוד:

<div class="code-panel" dir="ltr">

```python
env, agent, losses = train()
torch.save(agent.model.state_dict(), WEIGHTS_PATH)
print(f'Updates: {len(losses)}')
```

</div>

**פלט**

<div class="code-panel" dir="ltr">

```text
Updates: 112425
```

</div>

בהרצה של 30,000 המשחקים בוצעו 112,425 עדכוני משקלים, כשלושה או ארבעה בכל משחק (אחד לכל מהלך של X). ההרצה על המעבד, בלי GPU, נמשכה כ־13 דקות. ההפסד הממוצע ירד מכ־0.10 בעשירית הראשונה של האימון לכ־0.01 בעשירית האחרונה: הרשת מתקרבת ליעדים שהיא עצמה בונה. כפי שנראה מיד, זה עדיין אינו אומר כמה טוב היא משחקת.

הבודק יוצר רשת חדשה באותו מבנה, טוען את המשקלים ומעביר את הסוכן למצב ללא חקירה:

<div class="code-panel" dir="ltr">

```python
def test(path=WEIGHTS_PATH, games=1000, seed=100):
    env = TicTacToe()
    model = DQN()
    model.load_state_dict(torch.load(path, map_location='cpu', weights_only=True))
    agent = DQNAgent(env, model, training=False)
    return evaluate(env, agent.get_action, games=games, seed=seed)
```

</div>

`evaluate` היא פונקציית הבדיקה שכבר השתמשנו בה בפרקי האימון הטבלאי. היא משחקת 1,000 משחקים מול O אקראי וסופרת ניצחונות, הפסדים ותיקו; אין בה אימון או שינוי משקלים. כך נבדקת המדיניות של הסוכן לאחר הלמידה. עם המשקלים שנשמרו בהרצה שלמעלה התקבל:

**פלט**

<div class="code-panel" dir="ltr">

```text
{'wins': 990, 'losses': 3, 'draws': 7}
```

</div>

הסוכן ניצח ב־990 מתוך 1,000 משחקים, סיים 7 בתיקו והפסיד 3. התוצאה קרובה מאוד לזו של הסוכנים הטבלאיים מפרקים ד.8 ו־ד.10, אבל שימו לב להבדל הקטן: שם לא היה אף הפסד, וכאן יש שלושה. טבלה זוכרת כל לוח שראתה בנפרד; רשת מכלילה, ולכן על לוח נדיר, שדומה ללוחות אחרים אך דורש מהלך שונה, היא עלולה לטעות. זה המחיר של ההכללה, ובמשחקים גדולים הוא משתלם, כי שם טבלה כלל אינה אפשרית. הבדיקה נערכה עם זרע 100 מול יריב אקראי; הרצה עם זרעים אחרים תיתן מספרים מעט שונים.

כאן יש הבדל חשוב מחלק ג. שם, הפסד נמוך על נתוני הבדיקה היה מדד טוב לאיכות המודל, כי היעדים היו תוויות אמת. Loss נמוך אינו לבדו מדד ליכולת משחק: הוא מודד התאמה ליעדים שנבנו מהדגימות ומהרשת, ורשת יכולה להתאים היטב ליעדים שגויים שהיא עצמה ייצרה. ספירת התוצאות מול היריב בודקת את ההתנהגות בפועל. גם תוצאה טובה מול יריב אקראי אינה מוכיחה משחק מיטבי מול כל יריב.

<!-- editorlm-source-ref: [sources/RL/7.DQN_tic_tac_toe.pptx#L59-L61] -->

### הרצת הדוגמה וקוד המקור

שמרו את חמשת קובצי DQN המקושרים בראש הפרק לצד `ttt_env.py`, ‏`ttt_training.py` ו־`tabular_agent.py` מהפרקים הקודמים. בסביבת Python עם PyTorch הפעילו תחילה `dqn_train.py` ולאחריו `dqn_test.py`. הראשון יוצר את קובץ המשקלים, והשני טוען אותו ומדפיס את ספירות המשחקים.

קוד המקור המלא נמצא ב־[מאגר Tic_Tac_Toe_DQN בגרסה ששימשה להתאמה](https://github.com/MarkmanGilad/Tic_Tac_Toe_DQN/tree/659c4c8a635c83865334ee09863c061a94580518). עותק הספר שומר את רשת 11→128→64→1 ואת סדר רכיבי ההדגמה, עם התאמות לממשק המשותף וליעד DQN רגיל. לחומרי בניית משחקים ראו את חלק Pygame ואת [אתר הקורס](https://webprogramming.azurewebsites.net/Pages/RL/RL_Intro.aspx).

**מצב בדיקת הקוד:** הקוד המצורף הורץ כלשונו בסביבת Python עם PyTorch 2.11 על מעבד בלבד: אימון של 30,000 משחקים ולאחריו בדיקה של 1,000 משחקים. הפלטים שבפרק הם תוצאות ההרצה הזאת, וקובץ המשקלים שנוצר בה, [dqn_weights.pth](https://github.com/MarkmanGilad/book/blob/main/assets/rl/code/dqn_weights.pth), מצורף לקוד כדי שאפשר יהיה להריץ את הבודק גם בלי לאמן מחדש.

<nav class="book-nav" aria-label="ניווט בספר">
<a href="11-DQN.md">→ הקודם</a>
<a class="toc-link" href="../index.md">תוכן העניינים</a>
<a href="13-DDQN.md">הבא ←</a>
</nav>

</div>

<!-- editorlm-source-versions: {"schemaVersion": 1, "sources": {"sources/RL/7.DQN_tic_tac_toe.pptx": {"sourceSha256": "5720517684cefb9fae2c2b5976560edab6b1ddf1a856c60aff7e18213cbd4aec", "canonicalTextSha256": "a4b99a045c230d222e87f2f20a6e8c53f4ec8093dc1d3d124f664ae8b4350adb"}}} -->
