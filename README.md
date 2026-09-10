# Hunt The Code — CODE CRIME

Flask + SQLite debugging competition website for the DESPOTIX 2K26 / CODE CRIME symposium.

## Participant flow

1. Open the **HUNT THE CODE** front page.
2. Click **Enter the Event**.
3. Enter Team Name, Participant Name and Email.
4. Read the instructions and choose Set 1 or Set 2.
5. Enter the set password:
   - Set 1: `123`
   - Set 2: `456`
6. Start the 25-minute debugging challenge.
7. Use the Previous/Next arrows to move between questions.
8. Enter corrected code in the large editor. Dynamic line numbers support any number of lines.
9. Submit and return to the front page from the result page.

## Sets and scoring

- Set 1: Questions 1 and 2
- Set 2: Questions 3 and 4
- 2 questions per set
- 10 marks per question
- 4 hidden tests per question
- 2.5 marks per passed hidden test
- 20 marks maximum per set
- 25 minutes per set

## Admin

Admin page: `/admin`

Default admin password: `ADITYA`

The result sheet provides:

- **Show Answer (👁)** for each submission. The password is requested every time: `show@123`.
- **Download (⬇)** for each submission. No additional password is requested; the admin session is required. The download is an Excel `.xlsx` file containing participant details and submitted answers.
- Existing delete/dustbin password: `HEMA`.
- Existing Clear Leaderboard function remains protected by the dustbin password.
- Existing Download All Results Excel export remains available.

## Running on Windows

After extracting the ZIP:

```text
cd hunt_the_code
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

If the ZIP extracts a parent folder first, enter the folder that directly contains `app.py`.

## Important

The code execution feature uses a subprocess with a timeout. This is suitable for a controlled college-event LAN/demo environment, but it is **not a hardened hostile-code sandbox**. For public internet deployment, execute participant code inside isolated containers/VMs with no network access and strict CPU/memory/process limits.
