import tkinter as tk
import time
import random

# 將 C++ 程式碼分行寫成乾淨的清單，確保輸出絕對不會變亂碼
HACKER_LINES = [
    "#include <linux/module.h>",
    "#include <linux/kernel.h>",
    "#include <linux/init.h>",
    "#include <linux/fs.h>",
    "#include <linux/uaccess.h>",
    "",
    'MODULE_LICENSE("GPL");',
    'MODULE_AUTHOR("Hacker");',
    'MODULE_DESCRIPTION("Simulated Kernel Rootkit / Bypass");',
    "",
    '#define DEVICE_NAME "nexus_core"',
    "#define SUCCESS 0",
    "",
    "static int device_open(struct inode *inode, struct file *file) {",
    '    printk(KERN_INFO "nexus_core: Device opened by unauthorized PID\\n");',
    "    return SUCCESS;",
    "}",
    "",
    "static ssize_t device_read(struct file *file, char __user *buffer, size_t length, loff_t *offset) {",
    "    int bytes_read = 0;",
    '    char *secret_payload = "ACCESS GRANTED: Root privileges established.\\n";',
    "    ",
    "    while (length && *secret_payload) {",
    "        put_user(*(secret_payload++), buffer++);",
    "        length--;",
    "        bytes_read++;",
    "    }",
    "    return bytes_read;",
    "}",
    "",
    "static struct file_operations fops = {",
    "    .read = device_read,",
    "    .open = device_open,",
    "};",
    "",
    "static int __init hacker_init(void) {",
    '    printk(KERN_INFO "Injecting payload into memory ring 0...\\n");',
    "    // Bypassing firewall matrix...",
    "    return 0;",
    "}",
    "",
    "static void __exit hacker_exit(void) {",
    '    printk(KERN_INFO "Cleaning tracks and wiping syslog...\\n");',
    "}",
    "",
    "module_init(hacker_init);",
    "module_exit(hacker_exit);",
    
    "6767676767676767676767676767676767676767676767676767"
]

class CyberOpsDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBEROPS - Secure Terminal HUD")
        self.root.attributes('-fullscreen', True)  # 全螢幕
        self.root.configure(bg="#0b1315")  # 深色背景
        
        # 頂部狀態列
        self.top_frame = tk.Frame(root, bg="#0b1315", height=40)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        self.status_label = tk.Label(
            self.top_frame, 
            text="► CYBEROPS    🟢 ONLINE    SESSION 00:00:00    TARGET NETWORK: PHANTOM-11", 
            fg="#00ffcc", bg="#0b1315", font=("Consolas", 12, "bold")
        )
        self.status_label.pack(side=tk.LEFT)
        
        # 主佈局 (左右分割)
        self.main_frame = tk.Frame(root, bg="#0b1315")
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=5)
        
        # 左側：主要打字區 (HackerTyper)
        self.left_frame = tk.LabelFrame(
            self.main_frame, text=" . MAIN KERNEL STREAM ", 
            fg="#00ffcc", bg="#0b1315", font=("Consolas", 10, "bold")
        )
        self.left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        self.code_text = tk.Text(
            self.left_frame, bg="#060a0b", fg="#00ff00", 
            insertbackground="green", font=("Consolas", 12), wrap=tk.WORD
        )
        self.code_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.code_text.insert(tk.END, "=== SECURE SHELL ACTIVE. MASH ANY KEYS TO WRITE CODE. PRESS ESC TO EXIT. ===\n\n")
        
        # 右側：自動運作的酷炫特效區 (事件日誌與活動操作)
        self.right_frame = tk.Frame(self.main_frame, bg="#0b1315")
        self.right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # 右上：事件日誌 (Event Log)
        self.log_frame = tk.LabelFrame(
            self.right_frame, text=" . EVENT LOG ", 
            fg="#00ffcc", bg="#0b1315", font=("Consolas", 10, "bold")
        )
        self.log_frame.pack(expand=True, fill=tk.BOTH, pady=5)
        
        self.log_text = tk.Text(
            self.log_frame, bg="#060a0b", fg="#00aa88", 
            font=("Consolas", 9), height=15, wrap=tk.WORD
        )
        self.log_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        
        # 右下：背景進度條 (Active Operations)
        self.op_frame = tk.LabelFrame(
            self.right_frame, text=" . ACTIVE OPERATIONS ", 
            fg="#00ffcc", bg="#0b1315", font=("Consolas", 10, "bold")
        )
        self.op_frame.pack(expand=True, fill=tk.BOTH, pady=5)
        
        self.op_text = tk.Text(
            self.op_frame, bg="#060a0b", fg="#00ffcc", 
            font=("Consolas", 10), height=8, wrap=tk.WORD
        )
        self.op_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.init_operations()
        
        # 變數初始化
        self.line_index = 0
        self.char_in_line = 0
        self.start_time = time.time()
        
        # 綁定按鍵與背景定時更新
        self.root.bind("<Key>", self.on_key_press)
        self.update_hud()

    def init_operations(self):
        self.operations = [
            {"name": "Net recon", "progress": 12},
            {"name": "Discovery", "progress": 41},
            {"name": "Cred audit", "progress": 39},
            {"name": "Transfer backup", "progress": 9}
        ]
        self.refresh_operations_display()

    def refresh_operations_display(self):
        self.op_text.delete("1.0", tk.END)
        for op in self.operations:
            bar_blocks = "█" * (op["progress"] // 5) + "-" * (20 - (op["progress"] // 5))
            line = f"{op['name'].ljust(18)} [{bar_blocks}] {op['progress']:02d}%\n"
            self.op_text.insert(tk.END, line)

    def update_hud(self):
        # 更新上方計時器
        elapsed = int(time.time() - self.start_time)
        mins, secs = divmod(elapsed, 60)
        hours, mins = divmod(mins, 60)
        self.status_label.config(
            text=f"► CYBEROPS    🟢 ONLINE    SESSION {hours:02d}:{mins:02d}:{secs:02d}    TARGET NETWORK: PHANTOM-11"
        )
        
        # 自動增加右側的事件日誌
        if random.random() < 0.4:
            ip = f"{random.randint(10,200)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            actions = [
                f"[AUTH] MFA challenge pending on {ip}",
                f"[NODE] Service ssh open on {ip}",
                f"[XFER] vault_{random.randint(100,999)}.enc - {random.randint(1,90)}% ({random.randint(5,25)} MB/s)",
                f"[SYS] watchdog ok - heartbeat {random.randint(50,150)} ms",
                f"[DATA] ARP reply from {ip}"
            ]
            timestamp = time.strftime("%H:%M:%S")
            self.log_text.insert(tk.END, f"{timestamp}  {random.choice(actions)}\n")
            self.log_text.see(tk.END)
            
        # 隨機跳動右下角的進度條
        for op in self.operations:
            if random.random() < 0.2 and op["progress"] < 100:
                op["progress"] = min(100, op["progress"] + random.randint(1, 5))
        self.refresh_operations_display()
        
        self.root.after(800, self.update_hud)

    def on_key_press(self, event):
        # 按下 ESC 鍵退出全螢幕
        if event.keysym == "Escape":
            self.root.destroy()
            return
            
        # 每次按鍵，印出目前這行程式碼的接下來 4 個字元
        if self.line_index < len(HACKER_LINES):
            current_line = HACKER_LINES[self.line_index]
            
            # 如果這行還沒印完，就印出幾個字
            if self.char_in_line < len(current_line):
                chunk = current_line[self.char_in_line:self.char_in_line + 4]
                self.code_text.insert(tk.END, chunk)
                self.char_in_line += 4
            else:
                # 這行印完了，換行並移到下一行
                self.code_text.insert(tk.END, "\n")
                self.line_index += 1
                self.char_in_line = 0
        else:
            # 全部程式碼都印完後，重置並顯示重新注入提示
            self.line_index = 0
            self.char_in_line = 0
            self.code_text.insert(tk.END, "\n\n--- BUFFER RESET / RE-INJECTING PAYLOAD ---\n\n")
            
        self.code_text.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberOpsDashboard(root)
    root.mainloop()