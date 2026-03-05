import customtkinter as ctk
from tkinter import colorchooser, messagebox, filedialog
from PIL import Image, ImageTk
import json
import os
import sys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#  Локалізація / Localization
# ─────────────────────────────────────────────
LANG = {
    "en": {
        "title": "CTK Window Designer",
        "widgets": "🛠  WIDGETS",
        "wname_Button":      "Button",
        "wname_Label":       "Label",
        "wname_Entry":       "Entry",
        "wname_TextBox":     "TextBox",
        "wname_CheckBox":    "CheckBox",
        "wname_Switch":      "Switch",
        "wname_Slider":      "Slider",
        "wname_ProgressBar": "ProgressBar",
        "wname_Frame":       "Frame",
        "wname_ComboBox":    "ComboBox",
        "window_sect": "⚙  WINDOW",
        "win_title": "Title",
        "win_width": "Width",
        "win_height": "Height",
        "win_theme": "Theme",
        "win_bg": "BG Color",
        "win_icon": "Win Icon",
        "win_bgimg": "BG Image",
        "win_bgvid": "BG Video / GIF",
        "pick": "Pick",
        "browse": "Browse…",
        "clear_btn": "✕",
        "refresh": "🔄  Refresh",
        "clear_all": "🗑  Clear All",
        "canvas_hint": "CANVAS  —  drag widgets to position",
        "get_code": "⬇  GET CODE",
        "properties": "📋  PROPERTIES",
        "select_hint": "Select a widget\nto edit properties",
        "position": "Position",
        "apply_pos": "Apply position",
        "apply": "✔  Apply Changes",
        "delete": "🗑  Delete Widget",
        "copy": "📋  Copy to clipboard",
        "save_py": "💾  Save .py file",
        "close": "✕  Close",
        "clear_all_q": "Remove all widgets?",
        "copied": "Copied!",
        "copied_msg": "Code copied to clipboard.",
        "saved": "Saved!",
        "saved_msg": "Saved to:\n{}",
        "code_title": "Generated Python / CustomTkinter Code",
        "lang_label": "🌐 Language",
        "bg_scale": "BG Scale",
        "bg_opacity": "BG Opacity",
        "prop_text":          "Text",
        "prop_width":         "Width",
        "prop_height":        "Height",
        "prop_fg_color":      "Fill color",
        "prop_text_color":    "Text color",
        "prop_corner_radius": "Corner radius",
        "prop_placeholder":   "Placeholder",
        "prop_border_color":  "Border color",
        "prop_border_width":  "Border width",
        "prop_from_":         "Min value",
        "prop_to":            "Max value",
        "prop_value":         "Value",
        "prop_values":        "Options (CSV)",
        "theme_dark":   "dark",
        "theme_light":  "light",
        "theme_system": "system",
        "scale_fill":    "fill",
        "scale_fit":     "fit",
        "scale_stretch": "stretch",
        "path_hint": "path…",
    },
    "uk": {
        "title": "CTK Дизайнер вікон",
        "widgets": "🛠  ВІДЖЕТИ",
        "wname_Button":      "🖱  Кнопка",
        "wname_Label":       "🏷  Мітка",
        "wname_Entry":       "✏️  Поле введення",
        "wname_TextBox":     "📝  Текстова область",
        "wname_CheckBox":    "☑  Прапорець",
        "wname_Switch":      "🔀  Перемикач",
        "wname_Slider":      "🎚  Повзунок",
        "wname_ProgressBar": "📊  Прогрес-бар",
        "wname_Frame":       "🖼  Фрейм",
        "wname_ComboBox":    "📋  Випадний список",
        "window_sect": "⚙  ВІКНО",
        "win_title": "Заголовок",
        "win_width": "Ширина",
        "win_height": "Висота",
        "win_theme": "Тема",
        "win_bg": "Колір фону",
        "win_icon": "Іконка вікна",
        "win_bgimg": "Фон: зображення",
        "win_bgvid": "Фон: відео / GIF",
        "pick": "Вибір",
        "browse": "Огляд…",
        "clear_btn": "✕",
        "refresh": "🔄  Оновити",
        "clear_all": "🗑  Очистити все",
        "canvas_hint": "ПОЛОТНО  —  перетягуйте віджети",
        "get_code": "⬇  ОТРИМАТИ КОД",
        "properties": "📋  ВЛАСТИВОСТІ",
        "select_hint": "Оберіть віджет\nдля редагування",
        "position": "Позиція",
        "apply_pos": "Застосувати позицію",
        "apply": "✔  Застосувати",
        "delete": "🗑  Видалити віджет",
        "copy": "📋  Копіювати код",
        "save_py": "💾  Зберегти .py",
        "close": "✕  Закрити",
        "clear_all_q": "Видалити всі віджети?",
        "copied": "Скопійовано!",
        "copied_msg": "Код скопійовано в буфер обміну.",
        "saved": "Збережено!",
        "saved_msg": "Збережено до:\n{}",
        "code_title": "Згенерований Python / CustomTkinter код",
        "lang_label": "🌐 Мова",
        "bg_scale": "Масштаб фону",
        "bg_opacity": "Прозорість фону",
        "prop_text":          "Текст",
        "prop_width":         "Ширина",
        "prop_height":        "Висота",
        "prop_fg_color":      "Колір заливки",
        "prop_text_color":    "Колір тексту",
        "prop_corner_radius": "Радіус кутів",
        "prop_placeholder":   "Підказка",
        "prop_border_color":  "Колір рамки",
        "prop_border_width":  "Товщина рамки",
        "prop_from_":         "Мін. значення",
        "prop_to":            "Макс. значення",
        "prop_value":         "Значення",
        "prop_values":        "Опції (через кому)",
        "theme_dark":   "dark",
        "theme_light":  "light",
        "theme_system": "system",
        "scale_fill":    "fill",
        "scale_fit":     "fit",
        "scale_stretch": "stretch",
        "path_hint": "шлях…",
    },
}

WIDGET_DEFAULTS = {
    "Button":      {"text": "Button",   "width": 120, "height": 40,  "fg_color": "#1f6aa5", "text_color": "#ffffff", "corner_radius": 8},
    "Label":       {"text": "Label",    "width": 120, "height": 30,  "fg_color": "transparent", "text_color": "#ffffff"},
    "Entry":       {"placeholder": "Enter text…", "width": 200, "height": 35, "fg_color": "#2b2b2b", "text_color": "#ffffff", "border_color": "#555"},
    "TextBox":     {"width": 200, "height": 100, "fg_color": "#2b2b2b", "text_color": "#ffffff", "border_color": "#555"},
    "CheckBox":    {"text": "CheckBox", "width": 150, "height": 30,  "fg_color": "#1f6aa5", "text_color": "#ffffff"},
    "Switch":      {"text": "Switch",   "width": 150, "height": 30,  "fg_color": "#1f6aa5", "text_color": "#ffffff"},
    "Slider":      {"width": 200, "height": 20,  "from_": 0, "to": 100},
    "ProgressBar": {"width": 200, "height": 20,  "value": 0.5},
    "Frame":       {"width": 200, "height": 150, "fg_color": "#2b2b2b", "border_color": "#555", "border_width": 2, "corner_radius": 8},
    "ComboBox":    {"values": "Option 1,Option 2,Option 3", "width": 200, "height": 35},
}


class WidgetItem:
    _id_counter = 0

    def __init__(self, wtype, x, y):
        WidgetItem._id_counter += 1
        self.id = WidgetItem._id_counter
        self.wtype = wtype
        self.x = x
        self.y = y
        self.props = dict(WIDGET_DEFAULTS.get(wtype, {}))
        self.widget = None
        self.handle = None

class CTKDesigner(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lang_key = "uk"

        self.items: list[WidgetItem] = []
        self.selected: WidgetItem | None = None
        self._drag_start = None

        self.win_width_v   = ctk.IntVar(value=800)
        self.win_height_v  = ctk.IntVar(value=500)
        self.win_title_v   = ctk.StringVar(value="My Window")
        self.win_theme_v   = ctk.StringVar(value="dark")
        self.win_color_v   = ctk.StringVar(value="#1a1a2e")
        self.win_icon_v    = ctk.StringVar(value="")
        self.win_bgimg_v   = ctk.StringVar(value="")
        self.win_bgvid_v   = ctk.StringVar(value="")
        self.bg_scale_v    = ctk.StringVar(value="fill")
        self.bg_opacity_v  = ctk.DoubleVar(value=1.0)

        self._gif_frames: list = []
        self._gif_index  = 0
        self._gif_job    = None
        self._bg_label   = None

        self._build_ui()
        self._try_set_icon()

    def t(self, key):
        return LANG[self.lang_key].get(key, key)

    def _try_set_icon(self, path=None):
        candidates = [path, "icon.png",
                      os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "icon.png")]
        for p in candidates:
            if p and os.path.isfile(p):
                try:
                    img = Image.open(p).resize((64, 64), Image.LANCZOS)
                    self._app_icon_photo = ImageTk.PhotoImage(img)
                    self.iconphoto(True, self._app_icon_photo)
                    return
                except Exception:
                    pass

    def _build_ui(self):
        self.title(self.t("title"))
        self.geometry("1360x840")
        self.minsize(1100, 700)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_left()
        self._build_center()
        self._build_right()

    def _build_left(self):
        if hasattr(self, "_left_panel"):
            self._left_panel.destroy()
        self._left_panel = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#16213e")
        self._left_panel.grid(row=0, column=0, sticky="nsew")
        self._left_panel.grid_propagate(False)

        # Language switcher
        lang_bar = ctk.CTkFrame(self._left_panel, fg_color="#0d1830", corner_radius=6)
        lang_bar.pack(fill="x", padx=8, pady=(10, 4))
        ctk.CTkLabel(lang_bar, text=self.t("lang_label"),
                     font=("Consolas", 10), text_color="#4fc3f7").pack(side="left", padx=6)
        seg = ctk.CTkSegmentedButton(
            lang_bar, values=["🇬🇧 EN", "🇺🇦 UA"],
            command=self._switch_lang, width=120, height=26, font=("Consolas", 11))
        seg.set("🇺🇦 UA" if self.lang_key == "uk" else "🇬🇧 EN")
        seg.pack(side="right", padx=4, pady=4)

        body = ctk.CTkScrollableFrame(self._left_panel, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=4)

        ctk.CTkLabel(body, text=self.t("widgets"),
                     font=("Consolas", 13, "bold"), text_color="#4fc3f7").pack(pady=(8, 4))
        for wtype in WIDGET_DEFAULTS:
            label = self.t(f"wname_{wtype}")
            ctk.CTkButton(body, text=label, width=170, height=30,
                          fg_color="#0d3b66", hover_color="#1f6aa5", font=("Consolas", 12),
                          command=lambda t=wtype: self._add_widget(t)).pack(pady=2)

        ctk.CTkLabel(body, text="─────────────", text_color="#2a2a4a").pack(pady=4)
        ctk.CTkLabel(body, text=self.t("window_sect"),
                     font=("Consolas", 12, "bold"), text_color="#4fc3f7").pack(pady=(2, 4))

        for lk, var, w in [("win_title", self.win_title_v, 110),
                            ("win_width",  self.win_width_v,  65),
                            ("win_height", self.win_height_v, 65)]:
            r = ctk.CTkFrame(body, fg_color="transparent"); r.pack(pady=2)
            ctk.CTkLabel(r, text=self.t(lk), width=60, font=("Consolas", 10), anchor="w").pack(side="left")
            ctk.CTkEntry(r, textvariable=var, width=w, height=26, font=("Consolas", 10)).pack(side="left", padx=2)

        # Theme
        r = ctk.CTkFrame(body, fg_color="transparent"); r.pack(pady=2)
        ctk.CTkLabel(r, text=self.t("win_theme"), width=60, font=("Consolas", 10), anchor="w").pack(side="left")
        ctk.CTkOptionMenu(r, variable=self.win_theme_v, values=["dark", "light", "system"],
                          width=105, height=26, font=("Consolas", 10),
                          command=lambda v: ctk.set_appearance_mode(v)).pack(side="left", padx=2)

        # BG Color
        r = ctk.CTkFrame(body, fg_color="transparent"); r.pack(pady=2)
        ctk.CTkLabel(r, text=self.t("win_bg"), width=60, font=("Consolas", 10), anchor="w").pack(side="left")
        self._bg_color_preview = ctk.CTkLabel(r, text="", width=20, height=20,
                                              fg_color=self.win_color_v.get(), corner_radius=4)
        self._bg_color_preview.pack(side="left", padx=2)
        ctk.CTkButton(r, text=self.t("pick"), width=65, height=24, font=("Consolas", 10),
                      command=self._pick_win_bg).pack(side="left", padx=2)

        self._file_row(body, "win_icon",  self.win_icon_v,
                       [("Images","*.png *.ico *.jpg")], self._apply_win_icon)
        self._file_row(body, "win_bgimg", self.win_bgimg_v,
                       [("Images","*.png *.jpg *.jpeg *.bmp *.gif")], self._apply_bg_image)
        self._file_row(body, "win_bgvid", self.win_bgvid_v,
                       [("Video/GIF","*.gif *.mp4 *.avi *.mov")], self._apply_bg_video)

        r = ctk.CTkFrame(body, fg_color="transparent"); r.pack(pady=2)
        ctk.CTkLabel(r, text=self.t("bg_scale"), width=80, font=("Consolas", 10), anchor="w").pack(side="left")
        ctk.CTkOptionMenu(r, variable=self.bg_scale_v, values=["fill","fit","stretch"],
                          width=90, height=24, font=("Consolas", 10),
                          command=lambda v: self._reapply_bg()).pack(side="left", padx=2)

        r = ctk.CTkFrame(body, fg_color="transparent"); r.pack(pady=2)
        ctk.CTkLabel(r, text=self.t("bg_opacity"), width=80, font=("Consolas", 10), anchor="w").pack(side="left")
        ctk.CTkSlider(r, variable=self.bg_opacity_v, from_=0.1, to=1.0, width=90, height=16,
                      command=lambda v: self._reapply_bg()).pack(side="left", padx=2)

        ctk.CTkButton(body, text=self.t("refresh"), width=170, height=28,
                      fg_color="#0d3b66", font=("Consolas", 10),
                      command=self._refresh_canvas).pack(pady=(8, 2))
        ctk.CTkButton(body, text=self.t("clear_all"), width=170, height=28,
                      fg_color="#6b0f1a", hover_color="#a01020", font=("Consolas", 10),
                      command=self._clear_all).pack(pady=2)

    def _file_row(self, parent, label_key, var, ftypes, cb):
        outer = ctk.CTkFrame(parent, fg_color="#111827", corner_radius=6)
        outer.pack(fill="x", pady=3)
        ctk.CTkLabel(outer, text=self.t(label_key), font=("Consolas", 10),
                     text_color="#aaa", anchor="w").pack(anchor="w", padx=6, pady=(4, 0))
        row = ctk.CTkFrame(outer, fg_color="transparent"); row.pack(fill="x", padx=4, pady=(2, 4))
        ctk.CTkEntry(row, textvariable=var, width=104, height=24,
                     font=("Consolas", 9), placeholder_text=self.t("path_hint")).pack(side="left")
        ctk.CTkButton(row, text=self.t("browse"), width=52, height=24, font=("Consolas", 9),
                      command=lambda: self._browse(ftypes, var, cb)).pack(side="left", padx=2)
        ctk.CTkButton(row, text=self.t("clear_btn"), width=22, height=24, font=("Consolas", 9),
                      fg_color="#6b0f1a",
                      command=lambda: (var.set(""), cb(""))).pack(side="left")

    def _browse(self, ftypes, var, cb):
        p = filedialog.askopenfilename(filetypes=ftypes)
        if p:
            var.set(p)
            cb(p)

    def _switch_lang(self, val):
        self.lang_key = "uk" if "UA" in val else "en"
        self.title(self.t("title"))
        self._build_left()
        if hasattr(self, "_toolbar_lbl"):
            self._toolbar_lbl.configure(text=self.t("canvas_hint"))
        if hasattr(self, "_code_btn"):
            self._code_btn.configure(text=self.t("get_code"))
        if hasattr(self, "_props_title"):
            self._props_title.configure(text=self.t("properties"))
        self._show_props(self.selected)

    def _build_center(self):
        center = ctk.CTkFrame(self, corner_radius=0, fg_color="#0d0d1a")
        center.grid(row=0, column=1, sticky="nsew")
        center.grid_rowconfigure(1, weight=1)
        center.grid_columnconfigure(0, weight=1)

        toolbar = ctk.CTkFrame(center, height=44, fg_color="#111827", corner_radius=0)
        toolbar.grid(row=0, column=0, sticky="ew")
        self._toolbar_lbl = ctk.CTkLabel(toolbar, text=self.t("canvas_hint"),
                                          font=("Consolas", 12), text_color="#4fc3f7")
        self._toolbar_lbl.pack(side="left", padx=16)
        self._code_btn = ctk.CTkButton(toolbar, text=self.t("get_code"), width=160, height=32,
                                        fg_color="#0a7c59", hover_color="#0e9e72",
                                        font=("Consolas", 12, "bold"), command=self._show_code)
        self._code_btn.pack(side="right", padx=12, pady=6)

        wrap = ctk.CTkFrame(center, fg_color="#0d0d1a", corner_radius=0)
        wrap.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.canvas = ctk.CTkFrame(wrap,
                                   width=self.win_width_v.get(),
                                   height=self.win_height_v.get(),
                                   fg_color=self.win_color_v.get(),
                                   corner_radius=10,
                                   border_color="#2a2a4a", border_width=2)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")
        self.canvas.bind("<Button-1>", lambda e: self._select(None))

    def _build_right(self):
        self.right = ctk.CTkFrame(self, width=255, corner_radius=0, fg_color="#16213e")
        self.right.grid(row=0, column=2, sticky="nsew")
        self.right.grid_propagate(False)
        self._props_title = ctk.CTkLabel(self.right, text=self.t("properties"),
                                          font=("Consolas", 13, "bold"), text_color="#4fc3f7")
        self._props_title.pack(pady=(18, 8))
        self.props_frame = ctk.CTkScrollableFrame(self.right, fg_color="transparent")
        self.props_frame.pack(fill="both", expand=True, padx=8)
        self._show_props(None)

    def _scale_img(self, img: Image.Image) -> Image.Image:
        cw, ch = self.win_width_v.get(), self.win_height_v.get()
        m = self.bg_scale_v.get()
        if m == "stretch":
            return img.resize((cw, ch), Image.LANCZOS)
        elif m == "fit":
            img = img.copy(); img.thumbnail((cw, ch), Image.LANCZOS); return img
        else:  # fill
            r = max(cw / img.width, ch / img.height)
            nw, nh = int(img.width * r), int(img.height * r)
            img = img.resize((nw, nh), Image.LANCZOS)
            l, t = (nw - cw) // 2, (nh - ch) // 2
            return img.crop((l, t, l + cw, t + ch))

    def _apply_opacity(self, img: Image.Image) -> Image.Image:
        op = self.bg_opacity_v.get()
        if op >= 1.0: return img
        img = img.convert("RGBA")
        r, g, b, a = img.split()
        a = a.point(lambda p: int(p * op))
        return Image.merge("RGBA", (r, g, b, a))

    def _clear_bg(self):
        self._stop_gif()
        if self._bg_label:
            try: self._bg_label.place_forget(); self._bg_label.destroy()
            except Exception: pass
            self._bg_label = None

    def _show_static(self, img: Image.Image):
        img = self._apply_opacity(self._scale_img(img.convert("RGBA")))
        photo = ImageTk.PhotoImage(img)
        self._bg_label = ctk.CTkLabel(self.canvas, text="", image=photo)
        self._bg_label._photo = photo
        self._bg_label.place(x=0, y=0)
        self._bg_label.lower()

    def _apply_win_icon(self, path):
        if path: self._try_set_icon(path)

    def _apply_bg_image(self, path):
        self._clear_bg()
        if not path: return
        try:
            img = Image.open(path)
            try:
                img.seek(1); self._load_gif(path); return
            except EOFError:
                img.seek(0)
            self._show_static(img)
        except Exception as e:
            messagebox.showerror("❌ Помилка", str(e))

    def _apply_bg_video(self, path):
        self._clear_bg()
        if not path: return
        ext = os.path.splitext(path)[1].lower()
        if ext == ".gif":
            self._load_gif(path)
        else:
            self._load_video(path)

    def _reapply_bg(self):
        if self.win_bgvid_v.get():
            self._apply_bg_video(self.win_bgvid_v.get())
        elif self.win_bgimg_v.get():
            self._apply_bg_image(self.win_bgimg_v.get())

    def _load_gif(self, path):
        self._gif_frames = []
        try:
            src = Image.open(path)
            while True:
                f = self._apply_opacity(self._scale_img(src.convert("RGBA").copy()))
                self._gif_frames.append(ImageTk.PhotoImage(f))
                src.seek(src.tell() + 1)
        except EOFError:
            pass
        except Exception as e:
            messagebox.showerror("❌ Помилка", str(e)); return
        if not self._gif_frames: return
        self._bg_label = ctk.CTkLabel(self.canvas, text="", image=self._gif_frames[0])
        self._bg_label.place(x=0, y=0); self._bg_label.lower()
        self._gif_index = 0; self._animate_gif()

    def _animate_gif(self):
        if not self._gif_frames or not self._bg_label: return
        self._gif_index = (self._gif_index + 1) % len(self._gif_frames)
        self._bg_label.configure(image=self._gif_frames[self._gif_index])
        self._gif_job = self.after(80, self._animate_gif)

    def _stop_gif(self):
        if self._gif_job: self.after_cancel(self._gif_job); self._gif_job = None
        self._gif_frames = []

    def _load_video(self, path):
        try:
            import cv2
            cap = cv2.VideoCapture(path)
            frames = []
            while len(frames) < 150:
                ret, frame = cap.read()
                if not ret: break
                import numpy as np
                img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                f = self._apply_opacity(self._scale_img(img.convert("RGBA")))
                frames.append(ImageTk.PhotoImage(f))
            cap.release()
            if not frames: return
            self._gif_frames = frames
            self._bg_label = ctk.CTkLabel(self.canvas, text="", image=frames[0])
            self._bg_label.place(x=0, y=0); self._bg_label.lower()
            self._gif_index = 0; self._animate_gif()
        except ImportError:
            messagebox.showwarning("⚠ OpenCV не встановлено",
                "Для відтворення MP4/AVI встановіть:\n"
                "pip install opencv-python\n\n"
                "GIF-файли підтримуються без нього.")

    # ── Widget management ─────────────────────
    def _add_widget(self, wtype):
        item = WidgetItem(wtype, 30, 30 + len(self.items) * 55 % 400)
        self.items.append(item)
        self._render_item(item)
        self._select(item)

    def _render_item(self, item: WidgetItem):
        if item.widget: item.widget.place_forget(); item.widget.destroy()
        if item.handle: item.handle.place_forget(); item.handle.destroy()
        p = item.props; w = None
        try:
            match item.wtype:
                case "Button":
                    w = ctk.CTkButton(self.canvas, text=p.get("text","Button"),
                                      width=p["width"], height=p["height"],
                                      fg_color=p.get("fg_color","#1f6aa5"),
                                      text_color=p.get("text_color","#fff"),
                                      corner_radius=int(p.get("corner_radius",8)))
                case "Label":
                    w = ctk.CTkLabel(self.canvas, text=p.get("text","Label"),
                                     width=p["width"], height=p["height"],
                                     text_color=p.get("text_color","#fff"))
                case "Entry":
                    w = ctk.CTkEntry(self.canvas, placeholder_text=p.get("placeholder",""),
                                     width=p["width"], height=p["height"],
                                     fg_color=p.get("fg_color","#2b2b2b"),
                                     text_color=p.get("text_color","#fff"),
                                     border_color=p.get("border_color","#555"))
                case "TextBox":
                    w = ctk.CTkTextbox(self.canvas, width=p["width"], height=p["height"],
                                       fg_color=p.get("fg_color","#2b2b2b"),
                                       text_color=p.get("text_color","#fff"),
                                       border_color=p.get("border_color","#555"))
                case "CheckBox":
                    w = ctk.CTkCheckBox(self.canvas, text=p.get("text","CheckBox"),
                                        fg_color=p.get("fg_color","#1f6aa5"),
                                        text_color=p.get("text_color","#fff"))
                case "Switch":
                    w = ctk.CTkSwitch(self.canvas, text=p.get("text","Switch"),
                                      progress_color=p.get("fg_color","#1f6aa5"),
                                      text_color=p.get("text_color","#fff"))
                case "Slider":
                    w = ctk.CTkSlider(self.canvas, width=p["width"],
                                      from_=float(p.get("from_",0)), to=float(p.get("to",100)))
                case "ProgressBar":
                    w = ctk.CTkProgressBar(self.canvas, width=p["width"]); w.set(float(p.get("value",0.5)))
                case "Frame":
                    w = ctk.CTkFrame(self.canvas, width=p["width"], height=p["height"],
                                     fg_color=p.get("fg_color","#2b2b2b"),
                                     border_color=p.get("border_color","#555"),
                                     border_width=int(p.get("border_width",2)),
                                     corner_radius=int(p.get("corner_radius",8)))
                case "ComboBox":
                    vals = [v.strip() for v in p.get("values","Option 1").split(",")]
                    w = ctk.CTkComboBox(self.canvas, values=vals, width=p["width"], height=p["height"])
        except Exception:
            pass
        if w is None: return
        item.widget = w
        w.place(x=item.x, y=item.y)
        handle = ctk.CTkLabel(self.canvas, text="⠿", width=16, height=16,
                              fg_color="#1f6aa5", corner_radius=4,
                              font=("Consolas", 10), text_color="#fff", cursor="fleur")
        handle.place(x=item.x - 2, y=item.y - 18)
        item.handle = handle
        for obj in (w, handle):
            obj.bind("<ButtonPress-1>",  lambda e, it=item: self._drag_start_cb(e, it))
            obj.bind("<B1-Motion>",       lambda e, it=item: self._drag_motion_cb(e, it))
            obj.bind("<ButtonRelease-1>", lambda e, it=item: self._drag_end_cb(e, it))

    def _refresh_canvas(self):
        self.canvas.configure(width=self.win_width_v.get(),
                              height=self.win_height_v.get(),
                              fg_color=self.win_color_v.get())
        self._reapply_bg()
        for item in self.items: self._render_item(item)

    def _clear_all(self):
        if messagebox.askyesno("", self.t("clear_all_q")):
            for item in self.items:
                if item.widget: item.widget.destroy()
                if item.handle: item.handle.destroy()
            self.items.clear(); self.selected = None; self._show_props(None)

    def _drag_start_cb(self, e, item):
        self._drag_start = (e.x_root, e.y_root, item.x, item.y); self._select(item)

    def _drag_motion_cb(self, e, item):
        if not self._drag_start: return
        dx, dy = e.x_root - self._drag_start[0], e.y_root - self._drag_start[1]
        item.x = max(0, self._drag_start[2] + dx)
        item.y = max(0, self._drag_start[3] + dy)
        if item.widget: item.widget.place(x=item.x, y=item.y)
        if item.handle: item.handle.place(x=item.x - 2, y=item.y - 18)

    def _drag_end_cb(self, e, item): self._drag_start = None

    def _select(self, item):
        self.selected = item; self._show_props(item)

    # ── Properties panel ─────────────────────
    def _show_props(self, item):
        for c in self.props_frame.winfo_children(): c.destroy()
        if item is None:
            ctk.CTkLabel(self.props_frame, text=self.t("select_hint"),
                         text_color="#666", font=("Consolas", 11)).pack(pady=30)
            return

        ctk.CTkLabel(self.props_frame, text=f"[ {self.t('wname_' + item.wtype)} ]",
                     font=("Consolas", 13, "bold"), text_color="#4fc3f7").pack(pady=(8, 4))

        pf = ctk.CTkFrame(self.props_frame, fg_color="#111827", corner_radius=6)
        pf.pack(fill="x", pady=4, padx=2)
        ctk.CTkLabel(pf, text=self.t("position"), font=("Consolas", 11, "bold"),
                     text_color="#aaa").pack(anchor="w", padx=8, pady=(4, 0))
        pr = ctk.CTkFrame(pf, fg_color="transparent"); pr.pack(pady=4)
        self._pos_x = ctk.CTkEntry(pr, width=72, height=26, font=("Consolas", 11))
        self._pos_x.insert(0, str(item.x)); self._pos_x.pack(side="left", padx=4)
        ctk.CTkLabel(pr, text="×", font=("Consolas", 11)).pack(side="left")
        self._pos_y = ctk.CTkEntry(pr, width=72, height=26, font=("Consolas", 11))
        self._pos_y.insert(0, str(item.y)); self._pos_y.pack(side="left", padx=4)
        ctk.CTkButton(pf, text=self.t("apply_pos"), height=26, width=210,
                      font=("Consolas", 10),
                      command=lambda: self._apply_pos(item)).pack(pady=(0, 6))

        self._prop_vars = {}
        for key, val in item.props.items():
            row = ctk.CTkFrame(self.props_frame, fg_color="#111827", corner_radius=6)
            row.pack(fill="x", pady=2, padx=2)
            label_text = self.t(f"prop_{key}") if self.t(f"prop_{key}") != f"prop_{key}" else key
            ctk.CTkLabel(row, text=label_text, width=110, anchor="w",
                         font=("Consolas", 11), text_color="#ccc").pack(side="left", padx=6, pady=4)
            if "color" in key:
                pv = ctk.CTkLabel(row, text="", width=22, height=22,
                                  fg_color=str(val) if str(val) != "transparent" else "#333",
                                  corner_radius=4)
                pv.pack(side="left", padx=2)
                ctk.CTkButton(row, text=self.t("pick"), width=52, height=24, font=("Consolas", 10),
                              command=lambda k=key, p=pv, it=item: self._pick_color(it, k, p)
                              ).pack(side="left", padx=2)
            else:
                var = ctk.StringVar(value=str(val))
                self._prop_vars[key] = var
                ctk.CTkEntry(row, textvariable=var, width=110, height=26,
                             font=("Consolas", 11)).pack(side="right", padx=6, pady=4)

        ctk.CTkButton(self.props_frame, text=self.t("apply"), height=34,
                      fg_color="#0a7c59", hover_color="#0e9e72",
                      font=("Consolas", 12, "bold"),
                      command=lambda: self._apply_props(item)).pack(pady=10, fill="x", padx=2)
        ctk.CTkButton(self.props_frame, text=self.t("delete"), height=30,
                      fg_color="#6b0f1a", hover_color="#a01020",
                      font=("Consolas", 11),
                      command=lambda: self._delete_item(item)).pack(fill="x", padx=2)

    def _apply_pos(self, item):
        try:
            item.x = int(self._pos_x.get()); item.y = int(self._pos_y.get())
            if item.widget: item.widget.place(x=item.x, y=item.y)
            if item.handle: item.handle.place(x=item.x - 2, y=item.y - 18)
        except ValueError: pass

    def _apply_props(self, item):
        for key, var in self._prop_vars.items():
            v = var.get()
            try: item.props[key] = float(v) if "." in v else int(v)
            except ValueError: item.props[key] = v
        self._render_item(item); self._show_props(item)

    def _pick_color(self, item, key, pv):
        init = str(item.props.get(key, "#fff"))
        if init == "transparent": init = "#ffffff"
        c = colorchooser.askcolor(color=init, title=f"Pick: {key}")
        if c and c[1]:
            item.props[key] = c[1]; pv.configure(fg_color=c[1]); self._render_item(item)

    def _pick_win_bg(self):
        c = colorchooser.askcolor(color=self.win_color_v.get(), title="Window BG")
        if c and c[1]:
            self.win_color_v.set(c[1])
            self._bg_color_preview.configure(fg_color=c[1])
            self.canvas.configure(fg_color=c[1])

    def _delete_item(self, item):
        if item.widget: item.widget.destroy()
        if item.handle: item.handle.destroy()
        self.items.remove(item); self.selected = None; self._show_props(None)

    # ── Генератор Коду / Code generator ────────────────────────
    def _show_code(self):
        code = self._generate_code()
        win = ctk.CTkToplevel(self)
        win.title(self.t("code_title")); win.geometry("840x660"); win.grab_set()
        ctk.CTkLabel(win, text=self.t("code_title"),
                     font=("Consolas", 14, "bold"), text_color="#4fc3f7").pack(pady=(16, 6))
        tb = ctk.CTkTextbox(win, font=("Consolas", 12), wrap="none")
        tb.pack(fill="both", expand=True, padx=16, pady=(0, 8))
        tb.insert("1.0", code)
        br = ctk.CTkFrame(win, fg_color="transparent"); br.pack(pady=8)
        ctk.CTkButton(br, text=self.t("copy"), width=200, height=36, font=("Consolas", 12),
                      command=lambda: self._copy_code(code, win)).pack(side="left", padx=8)
        ctk.CTkButton(br, text=self.t("save_py"), width=170, height=36,
                      fg_color="#0a7c59", font=("Consolas", 12),
                      command=lambda: self._save_code(code)).pack(side="left", padx=8)
        ctk.CTkButton(br, text=self.t("close"), width=110, height=36,
                      fg_color="#333", font=("Consolas", 12),
                      command=win.destroy).pack(side="left", padx=8)

    def _copy_code(self, code, win):
        self.clipboard_clear(); self.clipboard_append(code)
        messagebox.showinfo(self.t("copied"), self.t("copied_msg"), parent=win)

    def _save_code(self, code):
        p = filedialog.asksaveasfilename(defaultextension=".py",
                                         filetypes=[("Python", "*.py"), ("All", "*.*")],
                                         initialfile="my_window.py")
        if p:
            with open(p, "w", encoding="utf-8") as f: f.write(code)
            messagebox.showinfo(self.t("saved"), self.t("saved_msg").format(p))

    def _generate_code(self) -> str:
        icon_p  = self.win_icon_v.get().replace("\\", "/")
        bgimg_p = self.win_bgimg_v.get().replace("\\", "/")
        bgvid_p = self.win_bgvid_v.get().replace("\\", "/")
        has_bg  = bool(bgimg_p or bgvid_p)
        bg_src  = bgvid_p or bgimg_p
        ext     = os.path.splitext(bg_src)[1].lower() if bg_src else ""
        is_video = ext in (".mp4", ".avi", ".mov")

        L = ["import customtkinter as ctk"]
        if has_bg or icon_p:
            L += ["from PIL import Image, ImageTk", "import os"]
        L += ["",
              f'ctk.set_appearance_mode("{self.win_theme_v.get()}")',
              'ctk.set_default_color_theme("blue")',
              "", "",
              "class MyWindow(ctk.CTk):",
              "    def __init__(self):",
              "        super().__init__()",
              f'        self.title("{self.win_title_v.get()}")',
              f'        self.geometry("{self.win_width_v.get()}x{self.win_height_v.get()}")',
              f'        self.configure(fg_color="{self.win_color_v.get()}")',
              ]

        if icon_p:
            L += ["",
                  "        # ── Window icon ──────────────────────",
                  f'        _ico = r"{icon_p}"',
                  "        if os.path.isfile(_ico):",
                  "            _img = Image.open(_ico).resize((64,64), Image.LANCZOS)",
                  "            self._icon_ph = ImageTk.PhotoImage(_img)",
                  "            self.iconphoto(True, self._icon_ph)",
                  ]

        if has_bg:
            L += ["",
                  "        # ── Background ───────────────────────",
                  "        self._gif_frames = []",
                  "        self._gif_idx = 0",
                  "        self._gif_job = None",
                  f'        self._load_bg(r"{bg_src}")',
                  ]

        L += ["", "        self._build_ui()", ""]

        if has_bg:
            L += ["    def _load_bg(self, path):",
                  "        if not os.path.isfile(path): return"]
            if is_video:
                L += ["        try:",
                      "            import cv2",
                      "            cap = cv2.VideoCapture(path)",
                      "            while len(self._gif_frames) < 150:",
                      "                ret, frame = cap.read()",
                      "                if not ret: break",
                      "                img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))",
                      f'                img = img.resize(({self.win_width_v.get()},{self.win_height_v.get()}), Image.LANCZOS)',
                      "                self._gif_frames.append(ImageTk.PhotoImage(img))",
                      "            cap.release()",
                      "        except ImportError: print('pip install opencv-python'); return",
                      ]
            else:
                L += ["        src = Image.open(path)",
                      "        try:",
                      "            while True:",
                      f'                f = src.convert(\"RGBA\").copy()',
                      f'                f = f.resize(({self.win_width_v.get()},{self.win_height_v.get()}), Image.LANCZOS)',
                      "                self._gif_frames.append(ImageTk.PhotoImage(f))",
                      "                src.seek(src.tell()+1)",
                      "        except EOFError: pass",
                      ]
            L += ["        if not self._gif_frames: return",
                  "        self._bg_lbl = ctk.CTkLabel(self, text='', image=self._gif_frames[0])",
                  "        self._bg_lbl.place(x=0, y=0); self._bg_lbl.lower()",
                  "        self._anim_bg()",
                  "",
                  "    def _anim_bg(self):",
                  "        if not self._gif_frames: return",
                  "        self._gif_idx = (self._gif_idx+1) % len(self._gif_frames)",
                  "        self._bg_lbl.configure(image=self._gif_frames[self._gif_idx])",
                  "        self._gif_job = self.after(80, self._anim_bg)",
                  "",
                  ]

        L.append("    def _build_ui(self):")

        if not self.items:
            L.append("        pass")
        else:
            for item in self.items:
                p = item.props
                v = f"self.{item.wtype.lower()}_{item.id}"
                match item.wtype:
                    case "Button":
                        L.append(f'        {v} = ctk.CTkButton(self, text="{p.get("text","Button")}", width={p["width"]}, height={p["height"]}, fg_color="{p.get("fg_color","#1f6aa5")}", text_color="{p.get("text_color","#fff")}", corner_radius={int(p.get("corner_radius",8))}, command=lambda: None)')
                    case "Label":
                        L.append(f'        {v} = ctk.CTkLabel(self, text="{p.get("text","Label")}", width={p["width"]}, height={p["height"]}, text_color="{p.get("text_color","#fff")}")')
                    case "Entry":
                        L.append(f'        {v} = ctk.CTkEntry(self, placeholder_text="{p.get("placeholder","")}", width={p["width"]}, height={p["height"]}, fg_color="{p.get("fg_color","#2b2b2b")}", text_color="{p.get("text_color","#fff")}", border_color="{p.get("border_color","#555")}")')
                    case "TextBox":
                        L.append(f'        {v} = ctk.CTkTextbox(self, width={p["width"]}, height={p["height"]}, fg_color="{p.get("fg_color","#2b2b2b")}", text_color="{p.get("text_color","#fff")}", border_color="{p.get("border_color","#555")}")')
                    case "CheckBox":
                        L.append(f'        {v} = ctk.CTkCheckBox(self, text="{p.get("text","CheckBox")}", fg_color="{p.get("fg_color","#1f6aa5")}", text_color="{p.get("text_color","#fff")}")')
                    case "Switch":
                        L.append(f'        {v} = ctk.CTkSwitch(self, text="{p.get("text","Switch")}", progress_color="{p.get("fg_color","#1f6aa5")}", text_color="{p.get("text_color","#fff")}")')
                    case "Slider":
                        L.append(f'        {v} = ctk.CTkSlider(self, width={p["width"]}, from_={p.get("from_",0)}, to={p.get("to",100)})')
                    case "ProgressBar":
                        L.append(f'        {v} = ctk.CTkProgressBar(self, width={p["width"]})')
                        L.append(f'        {v}.set({p.get("value",0.5)})')
                    case "Frame":
                        L.append(f'        {v} = ctk.CTkFrame(self, width={p["width"]}, height={p["height"]}, fg_color="{p.get("fg_color","#2b2b2b")}", border_color="{p.get("border_color","#555")}", border_width={int(p.get("border_width",2))}, corner_radius={int(p.get("corner_radius",8))})')
                    case "ComboBox":
                        vals = json.dumps([x.strip() for x in str(p.get("values","")).split(",")])
                        L.append(f'        {v} = ctk.CTkComboBox(self, values={vals}, width={p["width"]}, height={p["height"]})')
                L.append(f"        {v}.place(x={item.x}, y={item.y})")
                L.append("")

        L += ["", "",
              "if __name__ == '__main__':",
              "    app = MyWindow()",
              "    app.mainloop()"]
        return "\n".join(L)


if __name__ == "__main__":
    app = CTKDesigner()
    app.mainloop()