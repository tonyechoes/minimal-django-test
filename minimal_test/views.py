from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Minimal Django Test</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            .success { color: green; font-size: 24px; }
        </style>
    </head>
    <body>
        <h1 class="success">✅ Django 배포 성공!</h1>
        <p>최소 설정 테스트가 성공적으로 작동하고 있습니다.</p>
        <p>이제 원래 프로젝트의 문제를 찾을 수 있습니다.</p>
    </body>
    </html>
    """) 