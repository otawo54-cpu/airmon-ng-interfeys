# Airmon-ng Interfeys

Kali Linux (shu jumladan Live USB) uchun Wi-Fi adapterlarni **faqat diagnostika qilishga** mo‘ljallangan grafik boshqaruv paneli.

## Imkoniyatlar
- `iw dev` yordamida Wi-Fi interfeyslarni ko‘rish
- `ip -brief link` yordamida ulanish holatini tekshirish
- `lsusb` va `lsusb -t` bilan USB adapterlarni aniqlash
- `airmon-ng` bilan adapterlar ro‘yxatini ko‘rish
- `rfkill list` va `nmcli device status` yordamida muammolarni aniqlash
- Buyruqlar natijasini bitta oynada ko‘rish

**Cheklovlar:** Ushbu boshlang‘ich versiya xavfsiz diagnostika uchun. Monitor mode, deauth, handshake capture, parol buzish va begona tarmoqlarga aralashish funksiyalari yo‘q.

## Kali Linux Live USB da ishga tushirish

```bash
sudo apt update
sudo apt install -y git python3 python3-tk iw iproute2 usbutils rfkill network-manager aircrack-ng
git clone https://github.com/otawo54-cpu/airmon-ng-interfeys.git
cd airmon-ng-interfeys
python3 app.py
```

Yoki `bash run.sh` orqali ishga tushiring.

## Eslatma
Kali Live USB da persistence yoqilmagan bo‘lsa, dastur va o‘rnatilgan paketlar qayta yuklanganda yo‘qolishi mumkin. GitHub kodi esa saqlanadi.

Faqat o‘zingizga tegishli yoki sinovga ruxsat berilgan qurilmalarda ishlating. Ilovani ishga tushirish uchun root talab qilinmaydi.

## Loyiha tuzilmasi
- `app.py` — Tkinter grafik interfeys va diagnostika
- `run.sh` — ishga tushirish skripti
- `requirements.txt` — paketlar haqida ma’lumot
