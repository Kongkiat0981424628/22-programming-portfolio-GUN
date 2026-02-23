"""

โปรแกรมคำนวณเกรดจากคะแนน(A/B/C/D)
I : score = คะแนนสอบ (0–100)
P : score >= 80 เกรด A / 70-79 เกรด B / 60-69 เกรด C  / 50-59 เกรด D / 0-50 เกรด F
o : ช่วงคะแนนที่ได้ เกรดที่ได้
ตัวแปรที่ใช้ score int / float เก็บคะแนน grade string เกรด
ทำ HTML ใน Vscode ครับ
"""
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>โปรแกรมคำนวณเกรด</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            width: 350px;
            text-align: center;
        }

        h1 {
            color: #333;
        }

        input {
            width: 80%;
            padding: 10px;
            margin: 15px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
            text-align: center;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background-color: #4facfe;
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background-color: #00c6ff;
            transform: scale(1.05);
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }

        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: gray;
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>📊 โปรแกรมคำนวณเกรด</h1>
        <p>กรอกคะแนน (0 - 100)</p>

        <input type="number" id="score" placeholder="ใส่คะแนนของคุณ">

        <br>
        <button onclick="calculateGrade()">คำนวณเกรด</button>

        <div class="result" id="output"></div>

        <div class="footer">
            จัดทำโดย นายก้องเกียรติ ลาทอง ม.4/4 เลขที่22
        </div>
    </div>

    <script>
        function calculateGrade() {
            let score = parseFloat(document.getElementById("score").value);
            let grade = "";

            if (isNaN(score) || score < 0 || score > 100) {
                document.getElementById("output").innerHTML = "⚠ กรุณากรอกคะแนนระหว่าง 0 - 100";
                return;
            }

            if (score >= 80) {
                grade = "A";
            } else if (score >= 70) {
                grade = "B";
            } else if (score >= 60) {
                grade = "C";
            } else if (score >= 50) {
                grade = "D";
            } else {
                grade = "F";
            }

            document.getElementById("output").innerHTML =
                "คะแนนของคุณคือ: " + score + "<br>เกรดที่ได้คือ: " + grade;
        }
    </script>

</body>
</html>

