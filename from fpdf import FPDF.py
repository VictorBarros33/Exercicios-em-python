from fpdf import FPDF

class PDFColorido(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(30, 30, 100)
        self.cell(0, 12, 'Programação para Dispositivos Móveis - Android Studio (Java)', 0, 1, 'C')
        self.ln(2)

    def chapter_title(self, num, label):
        self.set_fill_color(100, 150, 200)
        self.set_text_color(255, 255, 255)
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, f'Capítulo {num}: {label}', 0, 1, 'L', fill=True)
        self.ln(2)

    def concept_box(self, title, text):
        self.set_fill_color(230, 240, 255)
        self.set_text_color(0, 0, 70)
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, title, 0, 1, 'L', fill=True)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, text)
        self.ln(3)

    def question_block(self, num, question, options, answer, comment):
        # Caixa da questão
        self.set_fill_color(255, 255, 230)
        self.set_text_color(0, 0, 0)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 8, f'Questão {num}:', 0, 1, 'L', fill=True)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, question)
        self.ln(1)
        # Opções
        self.set_fill_color(245, 245, 245)
        for i, opt in enumerate(options):
            self.cell(0, 7, f"{chr(97+i)}) {opt}", 0, 1, 'L', fill=True)
        self.ln(1)
        # Resposta e comentário
        self.set_fill_color(220, 255, 220)
        self.set_font('Arial', 'B', 11)
        self.cell(0, 7, f'Resposta correta: {answer}', 0, 1, 'L', fill=True)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, f'Comentário: {comment}')
        self.ln(5)

pdf = PDFColorido()
pdf.add_page()

pdf.chapter_title(1, "Resumo Teórico")

concepts = [
    ("Conceitos Básicos de Programação Móvel",
     "Mobilidade, características dos dispositivos móveis (tela sensível ao toque, bateria, sensores, GPS), sistema operacional Android."),
    ("Android Studio e Estrutura de Projetos",
     "IDE oficial, linguagem Java, arquivos principais: MainActivity.java, layouts XML, AndroidManifest.xml."),
    ("Componentes Principais do Android",
     "Activity, Intent, Service, BroadcastReceiver, ContentProvider."),
    ("Ciclo de Vida de uma Activity",
     "onCreate(), onStart(), onResume(), onPause(), onStop(), onDestroy()."),
    ("Layouts e Interface Gráfica",
     "Layouts XML: LinearLayout, RelativeLayout, ConstraintLayout; widgets: TextView, Button, EditText; eventos de clique."),
    ("Manipulação de Dados",
     "SharedPreferences, SQLite, arquivos internos/externos."),
    ("Permissões e Acesso a Recursos",
     "Declaração no manifest e solicitação em tempo de execução."),
    ("Intents e Navegação",
     "Intent explícita e implícita, startActivity(), startActivityForResult()."),
    ("Boas Práticas",
     "Interface simples, tratamento de erros, otimização de recursos, organização do código."),
    ("Exemplos Clássicos para Provas",
     "Apps simples como calculadora, lista de tarefas, uso de GPS, câmera.")
]

for i, (title, desc) in enumerate(concepts, 1):
    pdf.concept_box(f"{i}. {title}", desc)

pdf.add_page()
pdf.chapter_title(2, "Questões com Gabarito Comentado")

questions_with_answers = [
    {
        "question": "Qual o arquivo principal onde são declaradas permissões e componentes do app no Android?",
        "options": ["MainActivity.java", "activity_main.xml", "AndroidManifest.xml", "build.gradle"],
        "answer": "c) AndroidManifest.xml",
        "explanation": "O arquivo AndroidManifest.xml é o principal arquivo onde são declaradas as permissões necessárias e configurações do app."
    },
    {
        "question": "Qual dos seguintes métodos NÃO faz parte do ciclo de vida de uma Activity?",
        "options": ["onCreate()", "onPause()", "onReceive()", "onDestroy()"],
        "answer": "c) onReceive()",
        "explanation": "onReceive() é método de BroadcastReceiver, não da Activity."
    },
    {
        "question": "Qual é a finalidade da classe Intent no Android?",
        "options": ["Criar layouts", "Comunicar componentes", "Gerenciar banco de dados", "Armazenar dados na nuvem"],
        "answer": "b) Comunicar componentes",
        "explanation": "Intent é usada para comunicação e iniciar componentes (Activities, Services)."
    },
    {
        "question": "Qual dos layouts XML abaixo é usado para organizar elementos em linha ou coluna?",
        "options": ["RelativeLayout", "LinearLayout", "ConstraintLayout", "FrameLayout"],
        "answer": "b) LinearLayout",
        "explanation": "LinearLayout organiza elementos em linha ou coluna."
    },
    {
        "question": "Quando o método onPause() de uma Activity é chamado?",
        "options": ["Ao criar a Activity", "Quando a Activity vai para segundo plano", "Quando o app é finalizado", "Quando a Activity está visível"],
        "answer": "b) Quando a Activity vai para segundo plano",
        "explanation": "onPause() é chamado quando Activity perde o foco e vai para segundo plano."
    },
    {
        "question": "Qual recurso permite armazenar dados simples, como configurações do usuário?",
        "options": ["SQLite", "SharedPreferences", "ContentProvider", "Service"],
        "answer": "b) SharedPreferences",
        "explanation": "SharedPreferences armazena dados simples e persistentes."
    },
    {
        "question": "Para acessar a câmera, além da permissão no manifest, o que deve ser feito?",
        "options": ["Nada", "Pedir permissão em tempo de execução", "Usar startService()", "Salvar no banco"],
        "answer": "b) Pedir permissão em tempo de execução",
        "explanation": "Desde Android 6.0 é necessário pedir permissão em runtime."
    },
    {
        "question": "Qual método é usado para registrar evento de clique em botão?",
        "options": ["setOnClickListener()", "onClick()", "setOnTouchListener()", "onCreate()"],
        "answer": "a) setOnClickListener()",
        "explanation": "setOnClickListener() registra eventos de clique."
    },
    {
        "question": "Qual componente executa tarefas em segundo plano?",
        "options": ["Activity", "Service", "BroadcastReceiver", "Intent"],
        "answer": "b) Service",
        "explanation": "Service executa tarefas sem interface visual."
    },
    {
        "question": "Para navegar entre Activities, o que se deve fazer?",
        "options": ["Criar Intent explícita e chamar startActivity()", "Usar finish()", "Modificar AndroidManifest.xml", "Chamar onCreate() da próxima Activity"],
        "answer": "a) Criar Intent explícita e chamar startActivity()",
        "explanation": "Navegação entre Activities é feita via Intent explícita e startActivity()."
    }
]

for i, q in enumerate(questions_with_answers, 1):
    pdf.question_block(i, q["question"], q["options"], q["answer"], q["explanation"])

pdf.output("programacao_android_java_colorido.pdf")
print("PDF gerado com sucesso: programacao_android_java_colorido.pdf")
