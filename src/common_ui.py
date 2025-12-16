import sys
import webbrowser
import qtawesome as qta
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout, 
                             QWidget, QPushButton, QFrame, QHBoxLayout)
from PyQt6.QtCore import Qt, QMimeData, QPoint
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QFont, QPixmap, QCursor

APP_LINE = "AmbiToolbox"
BRAND_NAME = "Virtual Virgin"
URL_LINK = "[https://www.virtualvirgin.net/](https://www.virtualvirgin.net/)"
LOGO_PATH = "assets/vv_logo.png"

class Theme:
    DARK = {"bg": "#1E1E1E", "fg": "#E0E0E0", "panel": "#2D2D2D", "border": "#444444", "title_bg": "#252525"}
    LIGHT = {"bg": "#F5F5F5", "fg": "#333333", "panel": "#FFFFFF", "border": "#CCCCCC", "title_bg": "#EAEAEA"}

class TitleBar(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(50)
        self.setStyleSheet("background-color: transparent;")
        layout = QHBoxLayout(self)
        
        # A. BRAND LOGO (Local Asset)
        self.logo = QLabel()
        pixmap = QPixmap(LOGO_PATH)
        if not pixmap.isNull():
            self.logo.setPixmap(pixmap.scaledToHeight(30, Qt.TransformationMode.SmoothTransformation))
        else:
            self.logo.setText("VV") 
            self.logo.setStyleSheet(f"font-weight: bold; color: {parent.accent_color};")
        self.logo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.logo.mousePressEvent = lambda e: webbrowser.open(URL_LINK)
        layout.addWidget(self.logo)

        # B. TITLE
        title_box = QWidget()
        t_layout = QHBoxLayout(title_box)
        t_layout.setSpacing(5)
        lbl_line = QLabel(APP_LINE)
        lbl_line.setFont(QFont("Montserrat", 12))
        lbl_name = QLabel(parent.app_name)
        lbl_name.setFont(QFont("Jost", 14, QFont.Weight.Bold))
        lbl_name.setStyleSheet(f"color: {parent.accent_color};")
        t_layout.addWidget(lbl_line)
        t_layout.addWidget(lbl_name)
        layout.addWidget(title_box)
        layout.addStretch()

        # C. CONTROLS (Using Material Icons via qtawesome)
        self.theme_btn = QPushButton()
        self.update_theme_icon()
        self.theme_btn.clicked.connect(parent.toggle_theme)
        self.theme_btn.setStyleSheet("border: none;")
        layout.addWidget(self.theme_btn)
        
        btn_close = QPushButton()
        btn_close.setIcon(qta.icon('mdi.window-close', color='#888'))
        btn_close.clicked.connect(parent.close)
        btn_close.setStyleSheet("border: none;")
        layout.addWidget(btn_close)

    def update_theme_icon(self):
        # Toggles between Sunny and Night icon
        icon_name = 'mdi.weather-sunny' if self.parent.is_dark else 'mdi.weather-night'
        self.theme_btn.setIcon(qta.icon(icon_name, color='#888'))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.parent.old_pos = event.globalPosition().toPoint()
    def mouseMoveEvent(self, event):
        if hasattr(self.parent, 'old_pos'):
            delta = QPoint(event.globalPosition().toPoint() - self.parent.old_pos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.parent.old_pos = event.globalPosition().toPoint()

class DragDropArea(QFrame):
    def __init__(self, callback, accent):
        super().__init__()
        self.setAcceptDrops(True)
        self.callback = callback
        self.accent = accent
        self.setObjectName("DropZone")
        layout = QVBoxLayout(self)
        
        # Icon for Drop Zone (Material Design)
        self.icon_lbl = QLabel()
        self.icon_lbl.setPixmap(qta.icon('mdi.download', color='#666').pixmap(64, 64))
        self.icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.icon_lbl)
        
        self.label = QLabel("DROP FILE HERE")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            self.setStyleSheet(f"QFrame#DropZone {{ border: 2px solid {self.accent}; background-color: #333; }}")
            self.icon_lbl.setPixmap(qta.icon('mdi.download', color=self.accent).pixmap(64, 64))
        else:
            event.ignore()
    def dragLeaveEvent(self, event):
        self.parent().parent().apply_styles()
        self.icon_lbl.setPixmap(qta.icon('mdi.download', color='#666').pixmap(64, 64))
    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        if files: self.callback(files[0])

class AmbiToolboxApp(QMainWindow):
    def __init__(self, app_name, accent_color):
        super().__init__()
        self.app_name = app_name
        self.accent_color = accent_color
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(100, 100, 400, 450)
        self.is_dark = True

        container = QWidget()
        container.setObjectName("MainContainer")
        self.setCentralWidget(container)
        self.layout = QVBoxLayout(container)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.title_bar = TitleBar(self)
        self.layout.addWidget(self.title_bar)

        content = QWidget()
        self.content_layout = QVBoxLayout(content)
        self.content_layout.setContentsMargins(30, 20, 30, 30)
        
        self.drop_area = DragDropArea(self.process_file, accent_color)
        self.content_layout.addWidget(self.drop_area)
        
        self.options_area = QVBoxLayout()
        self.content_layout.addLayout(self.options_area)
        
        self.status = QLabel("Ready")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.content_layout.addWidget(self.status)
        
        self.layout.addWidget(content)
        self.apply_styles()

    def toggle_theme(self):
        self.is_dark = not self.is_dark
        self.title_bar.update_theme_icon()
        self.apply_styles()

    def apply_styles(self):
        t = Theme.DARK if self.is_dark else Theme.LIGHT
        self.setStyleSheet(f"""
            QMainWindow {{ background-color: {t['bg']}; border: 1px solid {t['border']}; }}
            QWidget#MainContainer {{ background-color: {t['bg']}; border: 1px solid {t['border']}; }}
            QLabel {{ color: {t['fg']}; font-family: 'Roboto'; }}
            QFrame#DropZone {{ background-color: {t['panel']}; border: 2px dashed {t['border']}; border-radius: 10px; }}
        """)
        self.title_bar.setStyleSheet(f"background-color: {t['title_bg']};")

    def process_file(self, file_path):
        pass # Override this