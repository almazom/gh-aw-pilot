# 🚀 Pilot Project — GH-AW Learning

Пилотный проект для изучения GitHub Agentic Workflows.

## 📁 Структура

```
pilot-project/
├── .github/
│   └── workflows/
│       └── hello-agent.md      ← Твой workflow (исходник)
├── .github-agentic/             ← Создаётся автоматически (после compile)
│   └── workflows/
│       └── hello-agent.yml     ← Сгенерированный Actions workflow
├── package-lock.json           ← Lock-файл (создаётся автоматически)
└── README.md                   ← Этот файл
```

## 🛠️ Быстрый старт

### 1. Инициализация репозитория
```bash
cd pilot-project
git init
git add .
git commit -m "Initial commit"
```

### 2. Установка GH-AW CLI
```bash
gh extension install github/gh-aw
gh aw --version
```

### 3. Компиляция workflow
```bash
gh aw compile
```

### 4. Проверка результата
```bash
ls -la .github-agentic/workflows/
# Должен появиться hello-agent.yml
```

### 5. Подключение к GitHub
```bash
# Создай репозиторий на GitHub (через UI или CLI)
gh repo create gh-aw-pilot --public --source=. --push
```

### 6. Тестирование
1. Открой Issues в своём репозитории на GitHub
2. Создай новый Issue
3. Напиши комментарий: `@agent hello`
4. Смотри в раздел **Actions** — workflow запустится
5. Через 10-20 секунд агент ответит в треде!

## 📊 Что происходит под капотом

```
Твой Markdown (.md)
       ↓
[gh aw compile] — AI анализирует инструкции
       ↓
Генерируется безопасный YAML
       ↓
GitHub Actions запускает workflow
       ↓
SafeOutputs проверяет результат
       ↓
Комментарий появляется в Issue ✅
```

## 🔍 Где смотреть

| Что | Где |
|-----|-----|
| Исходник workflow | `.github/workflows/hello-agent.md` |
| Сгенерированный YAML | `.github-agentic/workflows/hello-agent.yml` |
| Запуски | `https://github.com/[USER]/[REPO]/actions` |
| Результат | В комментариях Issue |

## 🎯 Следующие шаги

После успешного запуска:
1. Добавь новые инструменты (`tools: bash`, `web-search`)
2. Создай workflow на `issues: opened`
3. Попробуй ChatOps паттерн (команды в комментариях)

---

**Статус**: Готов к компиляции и тестированию! 🚀
