# import openai
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
# from .models import Code
#
#
# # Create your views here.
#
# def home(request):
#     lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup',
#                  'markup-templating', 'matlab', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex',
#                  'ruby', 'rust', 'sass', 'sql', 'swift', 'typescript']
#
#     if request.method == "POST":
#         code = request.POST['code']
#         lang = request.POST['lang']
#
#         # Перевірка чи вибрано мову
#         if lang == "Вибрати мову програмування":
#             messages.success(request, "Будь ласка, виберіть мову програмування.")
#             return render(request, 'home.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
#         else:
#             # OpenAI ключ
#             openai.api_key = "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"
#             # OpenAI екземпляр
#             openai.Model.list()
#             # Запит до OpenAI
#             try:
#                 response = openai.Completion.create(
#                     engine='text-davinci-003',
#                     prompt=f"Respond only with code. Fix this {lang} code: {code}",
#                     temperature=0,
#                     max_tokens=1000,
#                     top_p=1.0,
#                     frequency_penalty=0.0,
#                     presence_penalty=0.0,
#                 )
#                 # Парсинг відповіді
#                 response = (response["choices"][0]["text"]).strip()
#
#                 # Зберігання до бази даних
#                 record = Code(question=code, code_answer=response, language=lang, user=request.user)
#                 record.save()
#
#                 return render(request, 'home.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
#
#             except Exception as e:
#                 return render(request, 'home.html', {'lang_list': lang_list, 'response': e, 'lang': lang})
#
#     return render(request, 'home.html', {'lang_list': lang_list})
#
#
# def suggest(request):
#     lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'markup',
#                  'markup-templating', 'matlab', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex',
#                  'ruby', 'rust', 'sass', 'sql', 'swift', 'typescript']
#
#     if request.method == "POST":
#         code = request.POST['code']
#         lang = request.POST['lang']
#
#         # Перевірка чи вибрано мову
#         if lang == "Вибрати мову програмування":
#             messages.success(request, "Будь ласка, виберіть мову програмування.")
#             return render(request, 'suggest.html', {'lang_list': lang_list, 'code': code, 'lang': lang})
#         else:
#             # OpenAI ключ
#             openai.api_key = "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"
#             # OpenAI екземпляр
#             openai.Model.list()
#             # Запит до OpenAI
#             try:
#                 response = openai.Completion.create(
#                     engine='text-davinci-003',
#                     prompt=f"Respond only with code. {code}",
#                     temperature=0,
#                     max_tokens=1000,
#                     top_p=1.0,
#                     frequency_penalty=0.0,
#                     presence_penalty=0.0,
#                 )
#                 # Парсинг відповіді
#                 response = (response["choices"][0]["text"]).strip()
#
#                 # Зберігання до бази даних
#                 record = Code(question=code, code_answer=response, language=lang, user=request.user)
#                 record.save()
#
#                 return render(request, 'suggest.html', {'lang_list': lang_list, 'response': response, 'lang': lang})
#
#             except Exception as e:
#                 return render(request, 'suggest.html', {'lang_list': lang_list, 'response': e, 'lang': lang})
#
#     return render(request, 'suggest.html', {'lang_list': lang_list})
#
#
# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Ви увійшли у систему.")
#             return redirect('home')
#         else:
#             messages.success(request, "Помилка входу. Будь ласка спробуйте ще раз...")
#             return redirect('home')
#     else:
#         return render(request, 'home.html', {})
#
#
# def logout_user(request):
#     logout(request)
#     messages.success(request, "Ви вийшли з системи.")
#     return redirect('home')
#
#
# def register_user(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Ви зареєструвалися!  ")
#             return redirect('home')
#
#     else:
#         form = SignUpForm()
#
#     return render(request, 'register.html', {"form": form})
#
#
# def past(request):
#     if request.user.is_authenticated:
#         code = Code.objects.filter(user_id=request.user.id)
#         return render(request, 'past.html', {"code": code})
#     else:
#         messages.success(request, "Ви маєте бути авторизованим, щоб побачити попередній код")
#         return redirect('home')
#
#
# def delete_past(request, Past_id):
#     past = Code.objects.get(pk=Past_id)
#     past.delete()
#     messages.success(request, "Успішно видалено")
#     return redirect('past')

"""
Вюхи на класах
"""
#
#
# import openai
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm
# from .models import Code
#
#
# class CodeProcessor:
#     OPENAI_API_KEY = "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"
#
#     def __init__(self):
#         self.lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript',
#                           'markup',
#                           'markup-templating', 'matlab', 'objectivec', 'perl', 'php', 'powershell', 'python', 'r',
#                           'regex',
#                           'ruby', 'rust', 'sass', 'sql', 'swift', 'typescript']
#
#         self.openai_engine = 'text-davinci-003'
#
#     def get_openai_response(self, prompt):
#         openai.api_key = self.OPENAI_API_KEY
#         openai.Model.list()
#         response = openai.Completion.create(
#             engine=self.openai_engine,
#             prompt=prompt,
#             temperature=0,
#             max_tokens=1000,
#             top_p=1.0,
#             frequency_penalty=0.0,
#             presence_penalty=0.0,
#         )
#         return (response["choices"][0]["text"]).strip()
#
#     def process_code(self, request, template):
#         if request.method == "POST":
#             code = request.POST['code']
#             lang = request.POST['lang']
#
#             if lang == "Вибрати мову програмування":
#                 messages.success(request, "Будь ласка, виберіть мову програмування.")
#                 return render(request, template, {'lang_list': self.lang_list, 'code': code, 'lang': lang})
#
#             try:
#                 prompt = f"Respond only with code. Fix this {lang} code: {code}"
#                 response = self.get_openai_response(prompt)
#                 record = Code(question=code, code_answer=response, language=lang, user=request.user)
#                 record.save()
#                 return render(request, template,
#                               {'lang_list': self.lang_list, 'code': code, 'lang': lang, 'response': response})
#             except Exception as e:
#                 return render(request, template,
#                               {'lang_list': self.lang_list, 'code': code, 'lang': lang, 'response': e})
#
#         return render(request, template, {'lang_list': self.lang_list})
#
#
# class HomeView:
#     template_name = 'home.html'
#
#     def __init__(self):
#         self.code_processor = CodeProcessor()
#
#     def get(self, request):
#         return self.code_processor.process_code(request, self.template_name)
#
#     def post(self, request):
#         return self.code_processor.process_code(request, self.template_name)
#
#
# class SuggestView:
#     template_name = 'suggest.html'
#
#     def __init__(self):
#         self.code_processor = CodeProcessor()
#
#     def get(self, request):
#         return self.code_processor.process_code(request, self.template_name)
#
#     def post(self, request):
#         return self.code_processor.process_code(request, self.template_name)
#
#
# class LoginView:
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Ви увійшли у систему.")
#             return redirect('home')
#         else:
#             messages.success(request, "Помилка входу. Будь ласка спробуйте ще раз...")
#             return redirect('home')
#
#
# class LogoutView:
#     def get(self, request):
#         logout(request)
#         messages.success(request, "Ви вийшли з системи.")
#         return redirect('home')
#
#
# class RegisterView:
#     template_name = 'register.html'
#
#     def get(self, request):
#         form = SignUpForm()
#         return render(request, self.template_name, {"form": form})
#
#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, "Ви зареєструвалися!")
#             return redirect('home')
#         return render(request, self.template_name, {"form": form})
#
#
# class PastView:
#     template_name = 'past.html'
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             code = Code.objects.filter(user_id=request.user.id)
#             return render(request, self.template_name, {"code": code})
#         else:
#             messages.success(request, "Ви маєте бути авторизованим, щоб побачити попередній код")
#             return redirect('home')
#
#
# class DeletePastView:
#     def get(self, request, Past_id):
#         past = Code.objects.get(pk=Past_id)
#         past.delete()
#         messages.success(request, "Успішно видалено")
#         return redirect('past')


import openai
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Code

# Create your views here.

LANGUAGES = [
    'c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html',
    'java', 'javascript', 'markup', 'markup-templating', 'matlab',
    'objectivec', 'perl', 'php', 'powershell', 'python', 'r', 'regex',
    'ruby', 'rust', 'sass', 'sql', 'swift', 'typescript'
]


def get_openai_response(code, lang, prompt):
    openai.api_key = "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"
    openai.Model.list()

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return (response["choices"][0]["text"]).strip()
    except Exception as e:
        return str(e)


def render_home(request, template, context, prompt):
    if request.method == "POST":
        code = request.POST.get('code')
        lang = request.POST.get('lang')

        if lang == "Вибрати мову програмування":
            messages.success(request, "Будь ласка, виберіть мову програмування.")
        else:
            response = get_openai_response(code, lang, prompt)

            record = Code(question=code, code_answer=response, language=lang, user=request.user)
            record.save()

            context['response'] = response

    context['lang_list'] = LANGUAGES
    return render(request, template, context)


def home(request):
    prompt = "Respond only with code. Fix this {lang} code: {code}"
    return render_home(request, 'home.html', {'code': '', 'lang': ''}, prompt)


def suggest(request):
    prompt = "Suggest code improvements for this {lang} code: {code}"
    return render_home(request, 'suggest.html', {'code': '', 'lang': ''}, prompt)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ви увійшли у систему.")
        else:
            messages.success(request, "Помилка входу. Будь ласка спробуйте ще раз...")
    return redirect('home')


def logout_user(request):
    logout(request)
    messages.success(request, "Ви вийшли з системи.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Ви зареєструвалися!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})


def past(request):
    if request.user.is_authenticated:
        code = Code.objects.filter(user_id=request.user.id)
        return render(request, 'past.html', {"code": code})
    else:
        messages.success(request, "Ви маєте бути авторизованим, щоб побачити попередній код")
        return redirect('home')


def delete_past(request, Past_id):
    past = Code.objects.get(pk=Past_id)
    past.delete()
    messages.success(request, "Успішно видалено")
    return redirect('past')
