import os
import sys
import time
import secrets
from datetime import datetime

# ==========================================
# ANATTA-SCREEN: INVISIBLE SPECTRUM 20-COLOR
# ==========================================
C1, C2, C3, C4, C5   = '\033[38;5;255m', '\033[38;5;232m', '\033[38;5;240m', '\033[38;5;51m', '\033[38;5;226m'
C6, C7, C8, C9, C10  = '\033[38;5;196m', '\033[38;5;33m', '\033[38;5;93m', '\033[38;5;250m', '\033[38;5;235m'
C11, C12, C13, C14, C15 = '\033[38;5;201m', '\033[38;5;159m', '\033[38;5;21m', '\033[38;5;214m', '\033[38;5;118m'
C16, C17, C18, C19, C20 = '\033[38;5;234m', '\033[38;5;160m', '\033[38;5;39m', '\033[38;5;28m', '\033[38;5;252m'
RST, BLD = '\033[0m', '\033[1m'

# ==========================================
# LOGO: THE SHIELDED MONITOR (ANATTA)
# ==========================================
def anatta_banner_anim():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = f"""
    {C9}          _________________
    {C9}         |{C4}###############{C9}|
    {C9}         |{C4}## {C1}ANATTA {C4} ####{C9}|
    {C9}         |{C4}###############{C9}|
    {C10}         |_______|_______|
    {C10}                 |
    {C10}          _______|_______
    {C13}     [ SCREEN SHIELD v4.7 ]
    """
    print(logo)
    print(f"{C4}{BLD}   ANATTA-SCREEN: ANTI-CAPTURE & OVERLAY PROTECTION{RST}\n")
    
    # Shield activation animation
    for i in range(15):
        char = "▰" if i % 2 == 0 else "▱"
        sys.stdout.write(f"\r{C3}[{C11}SYNC{C3}] {C1}Engaging DisplayAffinity Protocol... {C4}{char * (i+1)}{RST}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\n{C15}[+] Secure Desktop Environment Established. Capture Blocked.{RST}\n")

# ==========================================
# ARCHITECTURE: ANTI-SCREENSHOT ENGINE
# ==========================================
class ScreenSentry:
    """Simulates screen capture prevention and forensic overlaying."""
    def __init__(self):
        self.protected_apps = ["CUI_Viewer.exe", "Secure_PDF_L4", "Finance_Vault"]
        self.session_id = f"SCR-{secrets.token_hex(3).upper()}"

    def monitor_os_events(self):
        """Simulates listening for 'PrintScreen' or Snipping Tool calls."""
        events = [
            ("User_Action", "Key_Press: PrintScreen"),
            ("System_Poll", "Active_Window: CUI_Viewer.exe"),
            ("Process_Alert", "SnippingTool.exe started"),
            ("User_Action", "Right-Click: Save Image As")
        ]
        
        for e_type, e_msg in events:
            time.sleep(1.2)
            self._handle_event(e_type, e_msg)

    def _handle_event(self, etype, emsg):
        ts = datetime.now().strftime("%H:%M:%S")
        print(f"{C10}[{C9}{ts}{C10}] {C12}{etype:<12} : {C1}{emsg}{RST}")
        
        if "PrintScreen" in emsg or "SnippingTool" in emsg:
            self._trigger_shield()
        elif "CUI_Viewer" in emsg:
            self._apply_forensic_overlay()

    def _trigger_shield(self):
        """Simulates darkening the window for capture tools."""
        print(f"\n{C6}{BLD}!!! CAPTURE ATTEMPT DETECTED: SHIELDING ACTIVE !!!{RST}")
        print(f"{C6}│ {C1}ACTION : {C10}Blanking Framebuffer via OS API{RST}")
        print(f"{C6}│ {C1}RESULT : {C2}{BLD}[ BLACK SCREEN CAPTURED ]{RST}")
        print(f"{C6}└{'─'*55}{RST}\n")
        time.sleep(0.5)

    def _apply_forensic_overlay(self):
        """Displays forensic watermark on the screen."""
        user = "Raj_Gautam"
        ip = "10.0.4.55"
        print(f"{C15}{BLD}[*] Applying Dynamic Forensic Overlay...{RST}")
        print(f"{C10}    >> {C11}WATERMARK: {user} | {ip} | {self.session_id} <<{RST}")
        print(f"{C3}    (Visible only on high-res capture/camera shots){RST}\n")

# ==========================================
# SIMULATION: PROTECTED SESSION
# ==========================================
def run_secure_session():
    anatta_banner_anim()
    sentry = ScreenSentry()
    
    print(f"{C13}[!] ENTERING PROTECTED CUI VIEWING ZONE...{RST}\n")
    sentry.monitor_os_events()
    
    print(f"{C15}[✔] Protected session ended. Screen affinity reset.{RST}")

if __name__ == "__main__":
    try:
        run_secure_session()
    except KeyboardInterrupt:
        print(f"\n{C6}[!] Shield Deactivated.{RST}")