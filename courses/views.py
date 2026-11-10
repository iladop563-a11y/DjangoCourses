from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Каталог курсів</title>
        </head>
        <body>
            <h1>Каталог курсів</h1>
            <p>Вітаємо на нашому навчальному сайті!</p>
            <h2>Доступні курси:</h2>
            <ul>
                <li>Основи Python</li>
                <li>Веброзробка на Django</li>
                <li>Основи HTML та CSS</li>
            </ul>
        </body>
        </html>
    """)