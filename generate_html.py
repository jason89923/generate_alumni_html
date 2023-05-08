import pandas as pd
import os

body = """
<!DOCTYPE html>
<html lang='en'>

<head>
    <meta charset='UTF-8'>
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css'>
    <link rel='stylesheet' href='./style.css'>
    <style>
        @import url('https://fonts.googleapis.com/css?family=Arvo');

        body,
        html {
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            width: 100%;
            height: 100%;
            background: #f5f4f4;
            font-size: 16px;
            font-family: 'Arvo', monospace;
        }

        @supports (display: grid) {

            body,
            html {
                display: block;
            }
        }

        .message {
            border: 1px solid #d2d0d0;
            padding: 2em;
            font-size: 1.7vw;
            box-shadow: -2px 2px 10px 0px rgba(68, 68, 68, 0.4);
        }

        @supports (display: grid) {
            .message {
                display: none;
            }
        }

        .section {
            display: none;
            padding: 2rem;
        }

        @media screen and (min-width: 768px) {
            .section {
                padding: 4rem;
            }
        }

        @supports (display: grid) {
            .section {
                display: block;
            }
        }

        h1 {
            font-size: 2rem;
            margin: 0 0 1.5em;
        }

        .grid {
            display: grid;
            grid-gap: 30px;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            grid-auto-rows: 150px;
            grid-auto-flow: row dense;
            border-radius: 5%;
        }

        .item {
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            box-sizing: border-box;
            grid-column-start: auto;
            grid-row-start: auto;
            background-position: center;
            box-shadow: -2px 2px 10px 0px rgba(68, 68, 68, 0.4);
            transition: transform 0.3s ease-in-out;
            cursor: pointer;
            counter-increment: item-counter;
            grid-row-end: span 2;
            grid-column-end: auto;
            border-radius: 5%;
        }


        .item:after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background-color: black;
            opacity: 0.3;
            transition: opacity 0.3s ease-in-out;
            border-radius: 5%;
        }

        .item:hover {
            transform: scale(1.05);
        }

        .item:hover:after {
            opacity: 0;
        }




        .item__details {
            position: relative;
            z-index: 1;
            padding: 15px;
            color: #444;
            background: #fff;
            text-transform: lowercase;
            letter-spacing: 1px;
            color: #828282;
            border-bottom-left-radius: 5%;
            border-bottom-right-radius: 5%;
        }

        .item__details:before {
            font-weight: bold;
            font-size: 1.1rem;
            padding-right: 0.5em;
            color: #444;
            border-bottom-left-radius: 5%;
            border-bottom-right-radius: 5%;
        }
    </style>
    <script>
        function openPopup(id) {
            var popups = document.querySelectorAll('.popup');
            for (var i = 0; i < popups.length; i++) {
                var popup = popups[i];
                if (popup.id === id) {
                    popup.classList.toggle('show');
                } else {
                    popup.classList.remove('show');
                }
            }
        }

        window.onclick = function (event) {
            var popups = document.querySelectorAll('.popup');
            for (var i = 0; i < popups.length; i++) {
                var popup = popups[i];
                if (event.target == popup) {
                    popup.classList.toggle('show');
                }
            }
        }
    </script>

    <style>
        @media screen and (max-width: 768px) {
            .popup {
                width: 90%;
                max-height: 90%;
            }
        }

        @media screen and (min-width: 769px) {
            .popup {
                width: 50%;
                max-height: 90%;
            }
        }

        @media screen and (min-width: 1200px) {
            .popup {
                width: 30%;
                max-height: 90%;
            }
        }

        .popup {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #fff;
            padding: 10px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
            z-index: 9999;
            max-width: 600px;
        }

        .show {
            display: block;
        }
    </style>
    <style>
        body {
            padding: 0;
            margin: 0;
            min-height: 40vh;
        }


        .about-dev {
            width: 100%;
            max-width: 40rem;
            margin: auto;
            box-shadow: 2px 4px 2px -2px rgba(0, 0, 0, .3), -2px -4px 15px -2px rgba(0, 0, 0, .2);
        }

        @-webkit-keyframes profile_in {
            0% {
                opacity: 0;
                transform: translateY(30%);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes profile_in {
            0% {
                opacity: 0;
                transform: translateY(30%);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }


        .profile-card_header-container {
            max-width: 15rem;
            margin: auto;
        }

        .profile-card_header {
            background: #272727;
            border-left: 0.625rem solid #97ece1;
            padding: 1.5em 1.5em 1em;
            text-align: center;
            max-height: 40vh;
        }


        .profile-card_header-imgbox {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 11rem;
            height: 11rem;
            overflow: hidden;
            border-radius: 50%;
            margin: auto;
            background: rgba(250, 214, 195, 1);
            border: 0.375rem solid rgba(250, 214, 195, 1);
        }

        .profile-card_header img {
            max-width: 100%;

        }


        .profile-card_header h1 {
            color: #f3f3f3;
            font-size: 1.5rem;
            margin-top: 0.8em;
            font-family: 'Oswald', sans-serif;
            font-weight: normal;
            position: relative;
        }

        .profile-card_header h1 span {
            font-size: 1.2rem;
            font-weight: 300;
            display: block;
            color: rgba(220, 220, 220, .95);
            margin-top: 0.25em;
            padding-top: 0.25em;
            border-top: 0.075em solid rgba(250, 214, 195, 1);
        }

        .profile-card_about {
            line-height: 2;
            background: #ededed;
            padding: 3rem;
            color: #222;
            font-family: 'Lato', sans-serif;
            font-size: 16px;
            overflow: scroll;
            max-height: 25vh;
        }

        .profile-card_about a {
            font-weight: 400;
            font-size: 16px;
            float: right;
        }

        .profile-card_about h2 {
            margin: 0;
            display: inline-block;
            color: #333;
            font-weight: normal;
            text-transform: uppercase;
            font-size: 1.3rem;
            position: relative;
            z-index: 2;
            vertical-align: middle;
        }

        .profile-card_about h2::before {
            content: '';
            position: absolute;
            width: 100%;
            height: 1rem;
            background: #c6f1eb;
            left: -5px;
            top: 50%;
            z-index: -1;
        }




        @media screen and (max-width: 26em) {
            .side_wrapper {
                min-height: 100vh;
                background: #ededed;
            }

            .about-dev {
                box-shadow: none;
            }
        }

        @media screen and (min-width: 33em) {
            .side_wrapper {
                margin: 2rem auto;
            }

        }

        @media screen and (min-height: 46em) {
            .side_wrapper {
                width: 100%;
                max-width: 26rem;
                margin: 0;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
            }

            .about-dev {
                max-width: 40rem;
            }
        }
    </style>
</head>


<body>
    <section class='section'>
        <div class='grid'>
"""

try:
    file_path = os.path.join(os.getcwd(), input('請輸入檔案名稱(不包含副檔名): ') + '.xlsx')
    data = pd.read_excel(file_path, engine='openpyxl')
except:
    print(f'找不到 {file_path} ，請將檔案放置於程式碼相同目錄中')
    os.system("pause")
    exit(1)

content_list = []
bubble_list = []
# 逐行讀取
for index, row in data.iterrows():
    img = row['img']
    url = row['url']
    title = row['title']
    content = row['content'].replace('\n', '<br>')
    type = row['type']
    content_list.append((index, img, title))
    bubble_list.append((index, index, img, title, content, url))


content = "<div onclick='openPopup(\"item_{}\")' class='item' style='background-image: url({}) ; background-size: contain ; background-repeat: no-repeat'> <div class='item__details'> {} </div> </div>"

bubble = "<div id='item_{}' class='popup'> <header class=\"profile-card_header\"> <a role='button' onclick='openPopup(\"item_{}\")' style=\" cursor: pointer; text-decoration:none; display: flex;justify-content: end;align-items: \
end; font-weight: 400; font-size: large; color: #ffffff;\">X</a> <div class=\"profile-card_header-container\"> <div class=\"profile-card_header-imgbox\"> <img src=\"{}\" /> \
</div> <h1>{}<span>特約商家</span></h1> </div> </header> <div class=\"profile-card_about\"> {} <br><br> <a role='button' href=\"{}\">More...</a> </div> </div>"


output_path = os.path.join(os.getcwd(), 'result.txt')
with open(output_path, "w", encoding='utf8') as f:
    print(body, file=f)
    for i in content_list:
        print(content.format(*i), file=f)
    print("</div> </section>", file=f)
    for i in bubble_list:
        print(bubble.format(*i), file=f)
    print("</body> </html>", file=f)
print(f'已將結果寫入 {output_path}，請將內容複製後到wordpress中貼上')
os.system("pause")