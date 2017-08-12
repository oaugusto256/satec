#! /usr/bin/env pyhton
# coding: latin-1
# Main

import sys,os

currentDir = os.getcwd()+'/Modulos'
sys.path.append(currentDir)

try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    import unicodedata,sip,interfaceTelecomunicacoes,interfaceSobre,interfaceIniciar,interfaceManual,interfaceGnuRadio
    from PyQt4.phonon import *
except:
    print ("SATEC - ERRO\nPor favor, Leia o README.TXT na pasta do programa para possiveis soluções de erros.\n")
    sys.exit(1)

class janelaSobre(QDialog, interfaceSobre.Ui_Dialog):
    def __init__(self, parent=None):
        super(janelaSobre, self).__init__(parent)
        self.setupUi(self)
        self.currentDir = os.getcwd()
    	self.labelLogo.setPixmap(QPixmap((self.currentDir+"/Imagens/Icones/logo.png")))

class janelaManual(QDialog, interfaceManual.Ui_Dialog):
    def __init__(self, parent= None):
        super(janelaManual, self).__init__(parent, Qt.WindowStaysOnTopHint)
        self.setupUi(self)
		
        self.checkBox.clicked.connect(self.checar)

    def checar(self):
        if self.checkBox.isChecked():
            currentDir = os.getcwd()
            checagem = currentDir+'/Temp/'+'checagem.txt'
            target = open(checagem, 'w')
            target.write('True')
            target.close()

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        janelaIniciar.manual.destroy()

class janelaIniciar(QDialog, interfaceIniciar.Ui_Dialog):
    def __init__(self, parent=None):
        super(janelaIniciar, self).__init__(parent)
        self.setupUi(self)
        self.currentDir = os.getcwd()
        self.setWindowTitle('SATEC - Iniciar')
        self.setWindowIcon(QIcon(self.currentDir+"/Imagens/Icones/icone.png"))
        self.label.setPixmap(QPixmap((self.currentDir+"/Imagens/Icones/logo.png")))

        # Conexão dos botões

        self.buttonTelecomunicacoes.clicked.connect(self.abrirJanelaTelecomunicacoes)
        self.buttonGnuRadio.clicked.connect(self.abrirJanelaGnuRadio)
        self.buttonFechar.clicked.connect(self.fechar)


    def abrirJanelaTelecomunicacoes(self):
        self.janelaApp = telecomunicacoes(self)
        self.manual = janelaManual(self)
        try:
            checagem = self.currentDir+'/Temp/'+'checagem.txt'
            condicao = open(checagem,'r')
            if condicao.read() == 'True':
                self.janelaApp.show()
                self.buttonTelecomunicacoes.setDisabled(True)
                self.buttonGnuRadio.setDisabled(True)
            else:
                self.manual.show()
                self.janelaApp.show()
                self.buttonTelecomunicacoes.setDisabled(True)
                self.buttonGnuRadio.setDisabled(True)
        except:
            self.manual.show()
            self.janelaApp.show()
            self.buttonTelecomunicacoes.setDisabled(True)
            self.buttonGnuRadio.setDisabled(True)


    def abrirJanelaGnuRadio(self):
        self.janelaApp = gnuradio(self)
        self.manual = janelaManual(self)
        try:
            checagem = self.currentDir+'/Temp/'+'checagem.txt'
            condicao = open(checagem,'r')
            if condicao.read() == 'True':
                self.janelaApp.show()
                self.buttonGnuRadio.setDisabled(True)
                self.buttonTelecomunicacoes.setDisabled(True)
            else:
                self.manual.show()
                self.janelaApp.show()
                self.buttonGnuRadio.setDisabled(True)
                self.buttonTelecomunicacoes.setDisabled(True)
        except:
            self.manual.show()
            self.janelaApp.show()
            self.buttonGnuRadio.setDisabled(True)
            self.buttonTelecomunicacoes.setDisabled(True)

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.msg = QMessageBox()
        self.msg.setWindowTitle('SATEC - Confirmação')
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setText('Deseja realmente fechar o programa ?')
        self.msg.addButton('Sim', QMessageBox.YesRole).clicked.connect(QApplication.quit)
        self.msg.addButton('Não', QMessageBox.NoRole)
        self.msg.exec_()

    def fechar(self, QCloseEvent):
        self.msg = QMessageBox()
        self.msg.setWindowTitle('SATEC - Confirmação')
        self.msg.setIcon(QMessageBox.Question)
        self.msg.setText('Deseja realmente fechar o programa ?')
        self.msg.addButton('Sim', QMessageBox.YesRole).clicked.connect(QApplication.quit)
        self.msg.addButton('Não', QMessageBox.NoRole)
        self.msg.exec_()

    def sim(self):
        janelaIniciar.janelaApp.destroy()
        self.buttonGnuRadio.setDisabled(False)
        self.buttonTelecomunicacoes.setDisabled(False)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- CLASSE TELECOMUNICAÇÔES ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class telecomunicacoes(QMainWindow, interfaceTelecomunicacoes.Ui_MainWindow):
    def __init__(self, parent=None):
        super(telecomunicacoes, self).__init__(parent)
        # Execução da interface
        self.setupUi(self)
        self.currentDir = os.getcwd()
        self.setWindowIcon(QIcon(self.currentDir+"/Imagens/Icones/icone.png"))

        self.tabWidget.setMovable(True)
        self.assunto = ''

        # Widgets escondidos no começo da execução
        self.listPossibles.hide()
        self.widgetEditarArvore.hide()

        #Objetos para o método relógio
        tempo = QTimer(self)
        tempo.timeout.connect(self.uptempo)
        tempo.start(1000)

        #Icones Gerais
        iconAbordagem = QIcon()
        iconVideoAula = QIcon()
        iconSimulacao = QIcon()
        iconExercicios = QIcon()
        iconReferencias = QIcon()
        iconProgramaExterno = QIcon()
        iconPlay = QIcon()
        iconPause = QIcon()
        iconPesquisar = QIcon()
        iconAdicionar = QIcon()
        iconDeletar = QIcon()
        iconSalvar = QIcon()
        
        #Icones do botão pesquisar e editar arvore
        iconPesquisar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/pesquisar.png'))
        self.buttonPesquisar.setIcon(iconPesquisar)      
        iconAdicionar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/adicionar.png'))
        self.buttonAdicionar.setIcon(iconAdicionar)        
        iconDeletar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/deletar.png'))
        self.buttonDeletar.setIcon(iconDeletar)      
        iconSalvar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/salvar.png'))
        self.buttonSalvar.setIcon(iconSalvar)      

        #Icones das abas
        iconAbordagem.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/abordagem.png'))
        self.tabWidget.setTabIcon(0, iconAbordagem)
        iconVideoAula.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/videoaula.png'))
        self.tabWidget.setTabIcon(1, iconVideoAula)
        iconSimulacao.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/simulacao.png'))
        self.tabWidget.setTabIcon(2, iconSimulacao)
        iconExercicios.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/exercicio.png'))
        self.tabWidget.setTabIcon(3, iconExercicios)
        iconReferencias.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/referencias.png'))
        self.tabWidget.setTabIcon(4, iconReferencias)
        iconProgramaExterno.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/programaexterno.png'))
        self.tabWidget.setTabIcon(5, iconProgramaExterno)

        #Icones reprodutor de video
        iconPlay.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/play.png'))
        iconPause.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/pause.png'))
        self.buttonReproduzir.setIcon(iconPlay)
        self.buttonPausar.setIcon(iconPause)

        # Grupo de botões da aba Programas Externos
        self.grupoButtons = QButtonGroup()
        self.grupoButtons.addButton(self.radioAudacity)
        self.grupoButtons.addButton(self.radioGedit)
        self.grupoButtons.addButton(self.radioGnu)
        self.grupoButtons.addButton(self.radioNavegador)

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------- Configurações da Árvore --------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

        self.treeAssuntos.headerItem().setText(0,"Árvore de assuntos")   
        
        if os.path.isfile('assuntosTelecomunicacoes.qfile'):
           self.listAssuntos = []
           file = QFile('assuntosTelecomunicacoes.qfile')
           file.open(QIODevice.ReadOnly)         
           dados = QDataStream(file)        
           filho = QTreeWidgetItem(self.treeAssuntos.invisibleRootItem())
           self.treeAssuntos.setItemExpanded(filho, True)
           self.treeAssuntos.setCurrentItem(filho,0) 
           filho.read(dados)
           numFilhos = dados.readUInt32()
           self.restaurarArvore(dados,filho,numFilhos)
        else:
           self.listAssuntos = []
           item = QTreeWidgetItem(self.treeAssuntos)
           item.setText(0,"Telecomunicações")
           self.treeAssuntos.insertTopLevelItem(0,item)
            
        self.buttonAdicionar.clicked.connect(self.adicionar)
        self.buttonDeletar.clicked.connect(self.deletar)
        self.buttonAdicionar.clicked.connect(self.verificarArvore)
        self.buttonDeletar.clicked.connect(self.verificarArvore)
        self.buttonSalvar.clicked.connect(self.salvar)

        self.connect(self.actionSobre_Qt, SIGNAL('triggered()'), qApp, SLOT('aboutQt()'))
        self.buttonSimular.clicked.connect(self.simular)
        self.buttonAbrir.clicked.connect(self.abrir)
        self.buttonPesquisar.clicked.connect(self.searchAssunto)
        self.treeAssuntos.itemClicked.connect(self.clickedAssunto)
        self.treeAssuntos.itemActivated.connect(self.clickedAssunto)
        self.actionSobre.triggered.connect(self.sobre)
        self.lineSearch.returnPressed.connect(self.buttonPesquisar.click)
        self.lineSearch.textEdited.connect(self.searchPossibles)
        self.listPossibles.itemClicked.connect(self.clickedPossible)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        self.buttonPausar.clicked.connect(self.pause)
        self.buttonReproduzir.clicked.connect(self.play)
        self.checkEdicao.stateChanged.connect(self.checarEstado)

    def verificarArvore(self):
        self.listAssuntos = []
        self.obterListaAssuntos(self.treeAssuntos.invisibleRootItem())
   
    def obterListaAssuntos(self,raiz):
       numFilhos = raiz.childCount()
       for i in range(0,numFilhos):
            filho = raiz.child(i)
            self.listAssuntos.append(str(unicode(filho.text(0).toUtf8(), encoding="UTF-8").encode('latin-1')))
            numFilhos = filho.childCount()
            self.obterListaAssuntos(filho)
    
    def checarEstado(self):     
        if self.checkEdicao.isChecked():
            QMessageBox.information(self, "SATEC - Atenção", "Modo de edição de árvore ativado.", "OK")
            self.widgetEditarArvore.show()
        else:
            self.widgetEditarArvore.hide()
    
    def adicionar(self):
        assunto = self.lineAdicionar.text()
        if  assunto != '':
            item = QTreeWidgetItem(self.treeAssuntos.currentItem())
            item.setText(0,assunto)
	    currentDir = os.getcwd()
	    os.mkdir(currentDir+'/Assuntos/'+assunto)
	    arquivo = open(currentDir+'/Assuntos/'+assunto+'/'+'abordagem.html','w')	
        self.lineAdicionar.clear()
        self.lineAdicionar.setFocus()       
    
    def deletar(self):
        if QMessageBox.question(self, "SATEC - Atenção", "Tem certeza que deseja apagar este item?", "Não", "Sim"):
            item = self.treeAssuntos.currentItem()
            if item != self.treeAssuntos.topLevelItem(0):
                sip.delete(item)
            else:
                QMessageBox.warning(self, "SATEC - Erro !", "Não há possibilidade de apagar a raiz da árvore.", "OK")

    def restaurarArvore(self,dados,item,numFilhos):
        for i in range(0, numFilhos):
            filho = QTreeWidgetItem(item)
            filho.read(dados)
            numFilhos = dados.readUInt32()
            self.listAssuntos.append(str(unicode(filho.text(0).toUtf8(), encoding="UTF-8").encode('latin-1')))
            self.restaurarArvore(dados,filho,numFilhos)

    def salvarAssuntos(self,item,dados):
        numFilhos = item.childCount()
        for i in range(0,numFilhos):
            filho = item.child(i)
            filho.write(dados)
            numFilhos = filho.childCount()
            dados.writeUInt32(numFilhos)
            self.salvarAssuntos(filho,dados)

    def salvar(self):
        file = QFile('assuntosTelecomunicacoes.qfile')
        file.open(QIODevice.WriteOnly)
        dados = QDataStream(file)
        QMessageBox.information(self, "SATEC - Informação", "Árvore de assuntos salvada com sucesso.", "OK")
        self.salvarAssuntos(self.treeAssuntos.invisibleRootItem(),dados)

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------- Ação ao clicar em algum item --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def clickedAssunto(self,item):
        try:
            self.textoComFormatacao = unicode(item.text(0).toUtf8(), encoding="UTF-8")
            self.assunto = unicode(item.text(0).toUtf8(), encoding="UTF-8")
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(telecomunicacoes, 'assunto')(self)
        except:
            self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados! \nInforme aos desenvolvedores.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Buscar assunto -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def searchAssunto(self):
        try:
            self.assunto= unicode(self.lineSearch.displayText().toUtf8(), encoding="UTF-8")
            researchedItem = self.treeAssuntos.findItems(self.assunto,Qt.MatchRecursive,0)
            item = researchedItem[0]
            item.setExpanded(True)
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(telecomunicacoes, 'assunto')(self)
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(self, 'SATEC - Erro',"Por favor, primeiro digite o assunto que queria pesquisar.", QMessageBox.Ok)
            else:
                self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados! \nTente novamente.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Buscar assunto sendo digitado --------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def searchPossibles(self):        
        self.listPossibles.clear()
        self.listPossibles.show()
        if unicode(self.lineSearch.text().toUtf8(), encoding="UTF-8").encode('latin-1').strip() == '':
            self.listPossibles.hide()
        for count in range(len(self.listAssuntos)):
            x = self.listAssuntos[count].find(unicode(self.lineSearch.text().toUtf8(), encoding="UTF-8").encode('latin-1'))
            if x == 0:
                self.listPossibles.addItem(self.listAssuntos[count])
                break
        if x != 0:
            self.listPossibles.addItem('Assunto não encontrado')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------- Executar assunto quando for clicado na barra de possibilidades -----------------------
# ----------------------------------------------------------------------------------------------------------------------

    def clickedPossible(self,item):
        try:
            self.textoComFormatacao = unicode(item.text().toUtf8(), encoding="UTF-8")
            self.assunto = unicode(item.text().toUtf8(), encoding="UTF-8")
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(telecomunicacoes, 'assunto')(self)
            self.listPossibles.clear()
            self.listPossibles.hide()
        except:
            self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados.\nInforme aos desenvolvedores.')

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Executar Assunto --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def assunto(self):
        self.tabWidget.setCurrentIndex(0)
        try:
            self.textAbordagem.setHtml(open(self.currentDir + '/Assuntos/%s/abordagem.html' % self.assunto).read())
            self.videoPlayer.load(Phonon.MediaSource(self.currentDir+'/Assuntos/%s/videoaula.3gp' % self.assunto))
            self.textExercicio.setHtml(open(self.currentDir + '/Assuntos/%s/exercicio.html' % self.assunto).read())
            self.textReferencias.setHtml(open(self.currentDir + '/Assuntos/%s/referencia.html' % self.assunto).read())
            self.statusbar.showMessage('Assunto %s aberto com sucesso!' % self.textoComFormatacao)
        except:
            self.textExercicio.setHtml('Assunto sem exercicio.')
            self.textReferencias.setHtml('Assunto sem referência no momento.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Ações do player de vídeo -------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def pause(self):
        self.videoPlayer.pause()

    def play(self):
        try:
            open(self.currentDir+'/Assuntos/%s/videoaula.3gp' % self.assunto)
            self.videoPlayer.play()
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(self, 'SATEC - Erro',"Por favor, primeiro clique em um assunto para reprodução da vídeo aula.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'SATEC - Erro',"Desculpe, Não existe vídeo aula para esse assunto.", QMessageBox.Ok)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Simulação GNU Radio  ---------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def simular(self):
        try:
            open(self.currentDir + '/Assuntos/%s/simulacao.py' % self.assunto)
            self.processo = QProcess()
            self.processo.start(self.currentDir + '/Assuntos/%s/simulacao.py' % self.assunto)
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(self, 'SATEC - Erro',"Por favor, primeiro clique em um assunto para realizar a sua simulação.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'SATEC - Erro',"Desculpe, Não existe simulação para esse assunto. ", QMessageBox.Ok)

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Função do relogio Relógio -----------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def uptempo(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        self.lcdNumber.display(text)

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Mensagem Confirmar Saída -------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def closeEvent(self, event):
        if QMessageBox.question(self, "SATEC - Confirmação", 'Deseja realmente fechar %s ?' % self.windowTitle(), "Não", "Sim"):
            event.ignore()            
            janelaIniciar.sim()
        else:
            event.ignore()

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Janela Sobre ----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def sobre(self):
        janela = janelaSobre(self)
        janela.show()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------- Ação botão Abrir - Programa Externos ---------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def abrir(self):
        button = self.grupoButtons.checkedButton()
        programa = str(button.text()).lower()
        if programa == 'gnu radio':
            programa = 'gnuradio-companion'
        if programa == 'navegador':
            programa = 'google-chrome'
        processo = QProcess()
        processo.startDetached(programa)

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- CLASSE GNU RADIO --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class gnuradio(QMainWindow,interfaceGnuRadio.Ui_MainWindow):
    def __init__(self, parent=None):
        super(gnuradio, self).__init__(parent)
         # Execução da interface
        self.setWindowTitle('Sistema de Aprendizagem - GNU Radio')
        self.setupUi(self)
        self.currentDir = os.getcwd()
        self.setWindowIcon(QIcon(self.currentDir+"/Imagens/Icones/icone.png"))

        self.tabWidget.setMovable(True)
        self.assunto = ''

        # Widgets escondidos no começo da execução
        self.listPossibles.hide()
        self.widgetEditarArvore.hide()

        #Objetos para o método relógio
        tempo = QTimer(self)
        tempo.timeout.connect(self.uptempo)
        tempo.start(1000)

        #Icones Gerais
        iconAbordagem = QIcon()
        iconVideoAula = QIcon()
        iconSimulacao = QIcon()
        iconExercicios = QIcon()
        iconReferencias = QIcon()
        iconProgramaExterno = QIcon()
        iconPlay = QIcon()
        iconPause = QIcon()
        iconPesquisar = QIcon()
        iconAdicionar = QIcon()
        iconDeletar = QIcon()
        iconSalvar = QIcon()
        
        #Icones do botão pesquisar e editar arvore
        iconPesquisar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/pesquisar.png'))
        self.buttonPesquisar.setIcon(iconPesquisar)      
        iconAdicionar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/adicionar.png'))
        self.buttonAdicionar.setIcon(iconAdicionar)        
        iconDeletar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/deletar.png'))
        self.buttonDeletar.setIcon(iconDeletar)      
        iconSalvar.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/salvar.png'))
        self.buttonSalvar.setIcon(iconSalvar)      

        #Icones das abas
        iconAbordagem.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/abordagem.png'))
        self.tabWidget.setTabIcon(0, iconAbordagem)
        iconVideoAula.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/videoaula.png'))
        self.tabWidget.setTabIcon(1, iconVideoAula)
        iconSimulacao.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/simulacao.png'))
        self.tabWidget.setTabIcon(2, iconSimulacao)
        iconExercicios.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/exercicio.png'))
        self.tabWidget.setTabIcon(3, iconExercicios)
        iconReferencias.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/referencias.png'))
        self.tabWidget.setTabIcon(4, iconReferencias)
        iconProgramaExterno.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/programaexterno.png'))
        self.tabWidget.setTabIcon(5, iconProgramaExterno)

        #Icones reprodutor de video
        iconPlay.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/play.png'))
        iconPause.addPixmap(QPixmap(self.currentDir+'/Imagens/Icones/pause.png'))
        self.buttonReproduzir.setIcon(iconPlay)
        self.buttonPausar.setIcon(iconPause)

        # Grupo de botões da aba Programas Externos
        self.grupoButtons = QButtonGroup()
        self.grupoButtons.addButton(self.radioAudacity)
        self.grupoButtons.addButton(self.radioGedit)
        self.grupoButtons.addButton(self.radioGnu)
        self.grupoButtons.addButton(self.radioNavegador)

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------- Configurações da Árvore --------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

        self.treeAssuntos.headerItem().setText(0,"Árvore de assuntos")  
        if os.path.isfile('assuntosGnuRadio.qfile'):
           self.listAssuntos = []
           file = QFile('assuntosGnuRadio.qfile')
           file.open(QIODevice.ReadOnly)         
           dados = QDataStream(file)        
           filho = QTreeWidgetItem(self.treeAssuntos.invisibleRootItem())
           self.treeAssuntos.setItemExpanded(filho, True)
           self.treeAssuntos.setCurrentItem(filho,0) 
           filho.read(dados)
           numFilhos = dados.readUInt32()
           self.restaurarArvore(dados,filho,numFilhos)
        else:
           self.listAssuntos = []
           item = QTreeWidgetItem(self.treeAssuntos)
           item.setText(0,"GNU Radio")
           self.treeAssuntos.insertTopLevelItem(0,item)
            
        self.buttonAdicionar.clicked.connect(self.adicionar)
        self.buttonDeletar.clicked.connect(self.deletar)
        self.buttonAdicionar.clicked.connect(self.verificarArvore)
        self.buttonDeletar.clicked.connect(self.verificarArvore)
        self.buttonSalvar.clicked.connect(self.salvar)

        self.connect(self.actionSobre_Qt, SIGNAL('triggered()'), qApp, SLOT('aboutQt()'))
        self.buttonSimular.clicked.connect(self.simular)
        self.buttonAbrir.clicked.connect(self.abrir)
        self.buttonPesquisar.clicked.connect(self.searchAssunto)
        self.treeAssuntos.itemClicked.connect(self.clickedAssunto)
        self.treeAssuntos.itemActivated.connect(self.clickedAssunto)
        self.actionSobre.triggered.connect(self.sobre)
        self.lineSearch.returnPressed.connect(self.buttonPesquisar.click)
        self.lineSearch.textEdited.connect(self.searchPossibles)
        self.listPossibles.itemClicked.connect(self.clickedPossible)
        self.seekSlider.setMediaObject(self.videoPlayer.mediaObject())
        self.volumeSlider.setAudioOutput(self.videoPlayer.audioOutput())
        self.buttonPausar.clicked.connect(self.pause)
        self.buttonReproduzir.clicked.connect(self.play)
        self.checkEdicao.stateChanged.connect(self.checarEstado)

    def verificarArvore(self):
        self.listAssuntos = []
        self.obterListaAssuntos(self.treeAssuntos.invisibleRootItem())
   
    def obterListaAssuntos(self,raiz):
       numFilhos = raiz.childCount()
       for i in range(0,numFilhos):
            filho = raiz.child(i)
            self.listAssuntos.append(str(unicode(filho.text(0).toUtf8(), encoding="UTF-8").encode('latin-1')))
            numFilhos = filho.childCount()
            self.obterListaAssuntos(filho)
    
    def checarEstado(self):     
        if self.checkEdicao.isChecked():
            QMessageBox.information(self, "SATEC - Atenção", "Modo de edição de árvore ativado.", "OK")
            self.widgetEditarArvore.show()
        else:
            self.widgetEditarArvore.hide()
    
    def adicionar(self):
        assunto = self.lineAdicionar.text()
        if  assunto != '':
            item = QTreeWidgetItem(self.treeAssuntos.currentItem())
            item.setText(0,assunto)
        self.lineAdicionar.clear()
        self.lineAdicionar.setFocus()

    def deletar(self):
        if QMessageBox.question(self, "SATEC - Atenção", "Tem certeza que deseja apagar este item?", "Não", "Sim"):
            item = self.treeAssuntos.currentItem()
            if item != self.treeAssuntos.topLevelItem(0):
                sip.delete(item)
            else:
                QMessageBox.warning(self, "SATEC - Erro ", "Não há possibilidade de apagar a raiz da árvore.", "OK")

    def restaurarArvore(self,dados,item,numFilhos):
        for i in range(0, numFilhos):
            filho = QTreeWidgetItem(item)
            filho.read(dados)
            numFilhos = dados.readUInt32()
            self.listAssuntos.append(str(unicode(filho.text(0).toUtf8(), encoding="UTF-8").encode('latin-1')))
            self.restaurarArvore(dados,filho,numFilhos)

    def salvarAssuntos(self,item,dados):
        numFilhos = item.childCount()
        for i in range(0,numFilhos):
            filho = item.child(i)
            filho.write(dados)
            numFilhos = filho.childCount()
            dados.writeUInt32(numFilhos)
            self.salvarAssuntos(filho,dados)

    def salvar(self):
        file = QFile('assuntosGnuRadio.qfile')
        file.open(QIODevice.WriteOnly)
        dados = QDataStream(file)
        QMessageBox.information(self, "SATEC - Informação", "Árvore de assuntos salvada com sucesso.", "OK")
        self.salvarAssuntos(self.treeAssuntos.invisibleRootItem(),dados)


# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------- Ação ao clicar em algum item na arvore --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def clickedAssunto(self,item):
        try:
            self.textoComFormatacao = unicode(item.text(0).toUtf8(), encoding="UTF-8")
            self.assunto = unicode(item.text(0).toUtf8(), encoding="UTF-8")
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(gnuradio, 'assunto')(self)
        except:
            self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados! \nInforme aos desenvolvedores.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Buscar assunto -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def searchAssunto(self):
        try:
            self.assunto= unicode(self.lineSearch.displayText().toUtf8(), encoding="UTF-8")
            researchedItem = self.treeAssuntos.findItems(self.assunto,Qt.MatchRecursive,0)
            item = researchedItem[0]
            item.setExpanded(True)
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(gnuradio, 'assunto')(self)
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(None,'SATEC - Erro ',"Por favor, primeiro digite o assunto que queria pesquisar.", QMessageBox.Ok)
            else:
                self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados! \nTente novamente.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Buscar assunto sendo digitado --------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def searchPossibles(self):
        self.listPossibles.clear()
        self.listPossibles.show()
        if unicode(self.lineSearch.text().toUtf8(), encoding="UTF-8").encode('latin-1').strip() == '':
            self.listPossibles.hide()
        for count in range(len(self.listAssuntos)):
            x = self.listAssuntos[count].find(unicode(self.lineSearch.text().toUtf8(), encoding="UTF-8").encode('latin-1'))
            if x == 0:
                self.listPossibles.addItem(self.listAssuntos[count])
                break
        if x != 0:
            self.listPossibles.addItem('Assunto não encontrado')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------- Executar assunto quando for clicado na barra de possibilidades -----------------------
# ----------------------------------------------------------------------------------------------------------------------

    def clickedPossible(self,item):
        try:
            self.textoComFormatacao = unicode(item.text().toUtf8(), encoding="UTF-8")
            self.assunto = unicode(item.text().toUtf8(), encoding="UTF-8")
            self.assunto = unicodedata.normalize('NFKD', self.assunto).encode('ascii','ignore')
            self.assunto = self.assunto.replace(' ','')
            getattr(gnuradio, 'assunto')(self)
            self.listPossibles.clear()
            self.listPossibles.hide()
        except:
            self.textAbordagem.setText('Não existe nada sobre esse assunto no banco de dados.\nInforme aos desenvolvedores.')


# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Executar Assunto --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def assunto(self):
        self.tabWidget.setCurrentIndex(0)
        try:
            self.textAbordagem.setHtml(open(self.currentDir + '/Assuntos/%s/abordagem.html' % self.assunto).read())
            self.videoPlayer.load(Phonon.MediaSource(self.currentDir+'/Assuntos/%s/videoaula.3gp' % self.assunto))
            self.textExercicio.setHtml(open(self.currentDir + '/Assuntos/%s/exercicio.html' % self.assunto).read())
            self.textReferencias.setHtml(open(self.currentDir + '/Assuntos/%s/referencia.html' % self.assunto).read())
            self.statusbar.showMessage('Assunto %s aberto com sucesso!' % self.textoComFormatacao)
        except:
            self.textExercicio.setHtml('Assunto sem exercicio.')
            self.textReferencias.setHtml('Assunto sem referência no momento.')

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Ações do player de vídeo -------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def pause(self):
        self.videoPlayer.pause()

    def play(self):
        try:
            open(self.currentDir+'/Assuntos/%s/videoaula.3gp' % self.assunto)
            self.videoPlayer.play()
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(None, 'SATEC - Erro !',"Por favor, primeiro clique em um assunto para reprodução da vídeo aula.", QMessageBox.Ok)
            else:
                QMessageBox.warning(None, 'SATEC - Erro !',"Desculpe, Não existe vídeo aula para esse assunto.", QMessageBox.Ok)


# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------------------- Simulação GNU Radio  ---------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def simular(self):
        try:
            open(self.currentDir + '/Assuntos/%s/simulacao.py' % self.assunto)
            self.processo = QProcess()
            self.processo.start(self.currentDir + '/Assuntos/%s/simulacao.py' % self.assunto)
        except:
            if self.assunto.strip() == '':
                QMessageBox.warning(self, 'SATEC - Erro !',"Por favor, primeiro clique em um assunto para realizar a sua simulação.", QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'SATEC - Erro !',"Desculpe, Não existe simulação para esse assunto. ", QMessageBox.Ok)


# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------- Relógio -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def uptempo(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        self.lcdNumber.display(text)

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Mensagem Confirmar Saída -------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def closeEvent(self, event):
        if QMessageBox.question(self, "SATEC - Confirmação", 'Deseja realmente fechar %s ?' % self.windowTitle(), "Não", "Sim"):
            event.ignore()            
            janelaIniciar.sim()
        else:
            event.ignore()

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------- Janela Sobre ----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def sobre(self):
        janela = janelaSobre(self)
        janela.show()

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------- Ação botão Abrir - Programa Externos ---------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

    def abrir(self):
        button = self.grupoButtons.checkedButton()
        programa = str(button.text()).lower()
        if programa == 'gnu radio':
            programa = 'gnuradio-companion' 
        if programa == 'navegador':
            programa = 'google-chrome'
        processo = QProcess()
        processo.startDetached(programa)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("SATEC")
    app.setQuitOnLastWindowClosed(True)     

    janelaIniciar = janelaIniciar()
    janelaIniciar.show()
    app.exec_()
