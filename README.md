# Yu-Gi-Oh! Monster Capsule Breed & Battle — bản dịch tiếng Việt

Bản vá (patch) Việt hoá cho trò chơi PlayStation 1 *Yu-Gi-Oh! Monster Capsule
Breed & Battle* (Konami, 1998, mã đĩa **SLPM-86096**, bản Nhật).

Đây là dự án của người hâm mộ, không liên quan tới Konami. Gói này **không
chứa** đĩa gốc hay bất kỳ dữ liệu nào của trò chơi. Bạn cần có ảnh đĩa gốc của
chính mình; bản vá chỉ ghi phần chữ tiếng Việt, phông chữ và vài byte mã điều
chỉnh lên ảnh đĩa đó.

Nội dung gói:

| File | Dùng để |
|---|---|
| `yugioh-mcbb-vi.ppf` | Bản vá, định dạng PPF 3.0 (chuẩn quen thuộc cho PS1) |
| `apply_patch.py` | Trình áp vá bằng Python, tự kiểm SHA-256 trước và sau |
| `README.md` | Hướng dẫn này |

---

## 1. Chuẩn bị ảnh đĩa gốc

Bạn cần ảnh đĩa dạng **`.bin` + `.cue`** (Mode 2, 2352 byte mỗi sector) của
đĩa Nhật SLPM-86096. Đây là định dạng mà các phần mềm đọc đĩa PS1 phổ biến
(ImgBurn, CDRDAO, Alcohol 120%…) xuất ra khi chọn kiểu "BIN/CUE". Một số lưu ý:

- Ảnh đĩa phải có **đúng một file `.bin`**. Nếu `.cue` của bạn liệt kê nhiều
  file (Track 01, Track 02…), đó là kiểu chia track, không dùng trực tiếp được.
- File `.iso` (2048 byte mỗi sector) **không** dùng được: bản vá tính theo
  sector 2352 byte có mã sửa lỗi.
- Kích thước đúng của `.bin`: **171.500.784 byte** (72.917 sector).

Bản vá được tạo từ đúng một ảnh đĩa; ảnh khác dù "cùng game" cũng có thể lệch
vài byte. Vì vậy phải kiểm SHA-256 trước khi áp.

## 2. Kiểm SHA-256 của ảnh đĩa gốc

SHA-256 là "dấu vân tay" của file: hai file giống nhau từng byte thì ra cùng
một chuỗi 64 ký tự. Ảnh đĩa gốc phải cho ra đúng:

```
51c38225b7e6e4af01f45aa3dd6209412ffb19c1f8569b667d038aca1141a355
```

Cách tính trên từng hệ điều hành (thay `TEN_FILE.bin` bằng tên file của bạn;
nếu đường dẫn có khoảng trắng thì đặt trong dấu ngoặc kép):

**Windows, dùng Command Prompt (cmd):**

```
certutil -hashfile "TEN_FILE.bin" SHA256
```

Mở cmd bằng cách gõ `cmd` vào ô tìm kiếm của Start; dùng lệnh `cd` để vào thư
mục chứa file, hoặc kéo thả file vào cửa sổ cmd để dán đường dẫn. Kết quả hiện
ở dòng thứ hai, có thể có khoảng trắng giữa các cặp ký tự, cứ bỏ khoảng trắng
mà so.

**Windows, dùng PowerShell:**

```
Get-FileHash "TEN_FILE.bin" -Algorithm SHA256
```

Cột `Hash` là kết quả (chữ in hoa, so không phân biệt hoa thường).

**macOS (Terminal):**

```
shasum -a 256 "TEN_FILE.bin"
```

**Linux:**

```
sha256sum "TEN_FILE.bin"
```

File 171 MB nên tính mất vài giây. Chỉ cần so **8 ký tự đầu** là đủ để nhận
ra: đĩa gốc đúng bắt đầu bằng `51c38225`. Nếu khác, xem mục 6.

## 3. Áp vá — cách 1: PPF-O-Matic (Windows, không cần cài gì)

PPF-O-Matic là công cụ nhỏ, miễn phí, chuyên áp bản vá PPF cho đĩa PS1; tìm
"PPF-O-Matic 3" trên các trang lưu trữ công cụ ROM hacking.

1. **Sao chép** file `.bin` gốc ra một bản khác, ví dụ `yugioh-mcbb-vi.bin`.
   PPF-O-Matic sửa thẳng vào file được chọn, nên luôn giữ lại bản gốc.
2. Mở PPF-O-Matic. Ô **ISO file**: chọn bản sao vừa tạo. Ô **Patch**: chọn
   `yugioh-mcbb-vi.ppf`.
3. Bấm **Apply**. Chỉ vài giây, chương trình báo "Successfully patched".
4. Kiểm lại theo mục 5.

## 4. Áp vá — cách 2: Python (Windows, macOS, Linux)

Cần Python 3 (tải từ python.org; trên Windows khi cài nhớ tick "Add Python to
PATH"). Cách này **không sửa** file gốc mà tạo file mới, và tự kiểm SHA-256.

1. Đặt `apply_patch.py`, `yugioh-mcbb-vi.ppf` và file `.bin` gốc vào cùng một
   thư mục.
2. Mở cmd / PowerShell / Terminal tại thư mục đó và chạy:

```
python apply_patch.py "TEN_FILE_GOC.bin" yugioh-mcbb-vi.ppf yugioh-mcbb-vi.bin
```

(Trên macOS/Linux nếu `python` không có thì dùng `python3`.)

3. Kịch bản kiểm SHA-256 của file gốc trước; nếu không đúng nó dừng lại và báo
   "Dia goc khong dung". Nếu đúng, nó ghi ra `yugioh-mcbb-vi.bin`, in SHA-256
   của file mới và báo `KHOP ban phat hanh` khi kết quả chuẩn.

## 5. Kiểm kết quả

Tính SHA-256 của file đã vá (cùng cách ở mục 2). Kết quả đúng:

```
9fd03ed2a3cd5661de41faa36388a38104411a36ab3754d383f27da212657830
```

Tức là bắt đầu bằng `9fd03ed2`. Đúng chuỗi này thì file của bạn giống từng
byte với bản đã được kiểm thử; mọi lỗi nếu có sẽ không phải do bước áp vá.

Sau đó tạo file `.cue` cho đĩa mới: sao chép file `.cue` gốc, đổi tên thành
`yugioh-mcbb-vi.cue`, mở bằng Notepad và sửa tên file `.bin` ở dòng đầu cho
khớp. Nội dung chuẩn chỉ có ba dòng:

```
FILE "yugioh-mcbb-vi.bin" BINARY
  TRACK 01 MODE2/2352
    INDEX 01 00:00:00
```

## 6. Khi SHA-256 không khớp

- **Ảnh gốc ra chuỗi khác `51c38225…`:** ảnh đĩa của bạn không phải bản mà bản
  vá được tạo từ đó. Nguyên nhân hay gặp: đọc đĩa ra kiểu `.iso` 2048 byte
  (kích thước sẽ nhỏ hơn 171 MB nhiều), đọc thiếu hoặc thừa sector cuối, đĩa
  thuộc bản in khác, hoặc file từng bị áp một bản vá khác. Cách chắc nhất là
  đọc lại từ đĩa thật bằng ImgBurn ở chế độ BIN/CUE. Bản vá áp lên ảnh sai vẫn
  chạy được phần lớn, nhưng có thể lỗi ở chỗ không lường trước.
- **Ảnh đã vá ra chuỗi khác `9fd03ed2…`:** bạn đã áp lên ảnh gốc sai (xem trên),
  hoặc áp hai lần lên cùng một file (PPF-O-Matic ghi thẳng, áp lại lần hai lên
  file đã vá thì vẫn ra đúng, nhưng áp lên file đã bị sửa khác thì không).
  Làm lại từ bản sao gốc.

## 7. Chạy trên giả lập

Mở file **`.cue`** (không phải `.bin`) bằng giả lập. Đã thử trên PCSX-Redux;
DuckStation, ePSXe, Mednafen/Beetle PSX đều đọc được BIN/CUE.

- Thẻ nhớ (save trong game) dùng bình thường, kể cả thẻ từ bản Nhật.
- **Không nạp save state** (lưu nhanh của giả lập, kiểu F5/F7) được tạo trên
  bản Nhật hay bản dịch cũ: save state giữ nguyên toàn bộ bộ nhớ lúc lưu, nên
  vẫn hiện chữ cũ dù đĩa mới đã đúng. Vào game bằng "Chơi tiếp" từ thẻ nhớ.
- Nếu từng chơi các bản dịch thử nghiệm phát hành trước tháng 9/2026, thú
  trong save cũ có thể mang chỉ số bị lỗi từ bản đó; nên nuôi vườn mới.
- Màn đặt tên thú: trang đầu là bảng chữ Việt (A–Z, Á Â Đ Í Ó Ư, số, dấu câu),
  hai trang Kana và ABC của bản gốc vẫn còn.

## 8. Câu hỏi thường gặp

**Có thể dùng bản vá xdelta không?** Gói này phát hành PPF vì là chuẩn lâu năm
cho PS1. Ai có sẵn hai ảnh đĩa có thể tự tạo xdelta bằng xdelta UI, kết quả
tương đương.

**Tại sao phải kiểm SHA-256 kỹ vậy?** Vì các lỗi khó chịu nhất (đứng máy, thú
tiến hoá sai) từng bắt nguồn từ chỉ vài byte lệch. Kiểm hash là cách duy nhất
biết chắc file của bạn giống file đã được thử.

**Báo lỗi ở đâu?** Mở issue trên repo này, kèm: SHA-256 của file đã vá, tên
giả lập, và ảnh chụp màn hình cùng câu thoại cuối cùng trước khi lỗi.

## 9. Bản quyền

Trò chơi, tên gọi, hình ảnh và âm thanh thuộc Konami và các chủ sở hữu liên
quan. Bản vá chỉ chứa phần chữ dịch, phông chữ vẽ lại và các byte mã điều
chỉnh, không phân phối dữ liệu gốc. Nếu chủ sở hữu bản quyền yêu cầu, bản vá
sẽ được gỡ.
