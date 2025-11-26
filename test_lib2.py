from pyhtmlkit import Body, Div
from pyhtmlkit.components import Text, Button, FileDialog, Input

# ---------- Callback Functions ----------
def encrypt_file():
    file_path = FileDialog.get_file("encryptFile")
    key = Input.get_text("encryptKey")

    if not file_path or not key:
        Text.set_text("encryptStatus", "❌ Select file & enter key first!")
    else:
        Text.set_text("encryptStatus", f"✅ File encrypted:\n{file_path}")

def decrypt_file():
    file_path = FileDialog.get_file("decryptFile")
    key = Input.get_text("decryptKey")

    if not file_path or not key:
        Text.set_text("decryptStatus", "❌ Select file & enter key first!")
    else:
        Text.set_text("decryptStatus", f"🔓 File decrypted:\n{file_path}")


# ---------- Main App Window ----------
app = Body(
    title="Encryptor",
    width=850,
    height=500,
    bg_color="#0f0f0f"
)

# ----------- Title -----------
Text(
    text="🔐 File Encryptor",
    font_size=28,
    color="#22c55e",
    pady=20
)

# ----------- Wrapper Row (Left & Right Panels) -----------
Div(
    width=800,
    height=350,
    bg_color=None,
    children=[]
)

# ------------ ENCRYPT PANEL ------------
Div(
    width=380,
    height=330,
    padding=20,
    bg_color="#1a1a1a",
    corner_radius=12,
    children=[
        Text("Encrypt File", font_size=20, color="#22c55e", pady=10),

        FileDialog(
            id="encryptFile",
            width=320,
            height=40,
            placeholder="Choose file to encrypt",
            frame_bg="#111111",
            entry_bg="#0f0f0f",
            entry_text_color="#e5e5e5",
            button_color="#22c55e",
            button_text_color="black",
            pady=10
        ),

        Input(
            id="encryptKey",
            width=320,
            height=40,
            placeholder="Enter encryption key",
            bg_color="#0f0f0f",
            text_color="#e5e5e5",
            pady=10
        ),

        Button(
            text="Encrypt",
            width=150,
            height=40,
            color="#22c55e",
            hover_color="#16a34a",
            text_color="black",
            on_click=encrypt_file,
            pady=15
        ),

        Text(id="encryptStatus", text="", color="#9ef6c5", font_size=14)
    ]
)

# ------------ DECRYPT PANEL ------------
Div(
    width=380,
    height=330,
    padding=20,
    bg_color="#1a1a1a",
    corner_radius=12,
    children=[
        Text("Decrypt File", font_size=20, color="#22c55e", pady=10),

        FileDialog(
            id="decryptFile",
            width=320,
            height=40,
            placeholder="Choose file to decrypt",
            frame_bg="#111111",
            entry_bg="#0f0f0f",
            entry_text_color="#e5e5e5",
            button_color="#22c55e",
            button_text_color="black",
            pady=10
        ),

        Input(
            id="decryptKey",
            width=320,
            height=40,
            placeholder="Enter decryption key",
            bg_color="#0f0f0f",
            text_color="#e5e5e5",
            pady=10
        ),

        Button(
            text="Decrypt",
            width=150,
            height=40,
            color="#22c55e",
            hover_color="#16a34a",
            text_color="black",
            on_click=decrypt_file,
            pady=15
        ),

        Text(id="decryptStatus", text="", color="#9ef6c5", font_size=14)
    ]
)


app.run()
