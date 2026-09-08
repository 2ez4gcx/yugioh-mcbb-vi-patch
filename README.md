# Yu-Gi-Oh! Monster Capsule Breed & Battle — bản dịch tiếng Việt

Bản vá (patch) Việt hoá cho trò chơi PlayStation *Yu-Gi-Oh! Monster Capsule
Breed & Battle* (Konami, 1998, mã đĩa SLPM-86096). Đây là dự án của người hâm
mộ, không liên quan tới Konami. Gói này **không chứa** đĩa gốc hay bất kỳ dữ
liệu nào của trò chơi; bạn cần có đĩa gốc của mình.

## Cần có

- File ảnh đĩa gốc bản Nhật, định dạng `.bin` (Mode 2 / 2352 byte mỗi sector)
  kèm `.cue`. Kiểm bằng SHA-256, phải đúng:

  ```
  51c38225b7e6e4af01f45aa3dd6209412ffb19c1f8569b667d038aca1141a355
  ```

  Trên Windows: `certutil -hashfile <ten_file>.bin SHA256`.
- Một trong hai cách áp vá: **PPF-O-Matic** (Windows), hoặc Python 3 với
  `apply_patch.py` kèm theo.

## Áp vá

Cách 1, PPF-O-Matic: chọn file `.bin` gốc và `yugioh-mcbb-vi.ppf`, bấm Apply.
Nên áp lên một **bản sao** của đĩa gốc.

Cách 2, Python:

```
python apply_patch.py <dia_goc>.bin yugioh-mcbb-vi.ppf yugioh-mcbb-vi.bin
```

Kịch bản kiểm SHA-256 của đĩa gốc trước khi áp và báo kết quả sau khi áp.
Đĩa sau khi vá phải có SHA-256:

```
9fd03ed2a3cd5661de41faa36388a38104411a36ab3754d383f27da212657830
```

Dùng lại file `.cue` của đĩa gốc, đổi tên file `.bin` trong đó cho khớp.

## Lưu ý khi chơi

- Save trên **thẻ nhớ** dùng bình thường. Không nạp *save state* của giả lập
  được lưu trên bản cũ hay bản Nhật: save state giữ nguyên mã và chữ đang nằm
  trong bộ nhớ lúc lưu, nên vẫn hiện chữ cũ dù đĩa đã mới.
- Ở màn đặt tên thú, trang đầu là bảng chữ Việt (A–Z, Á Â Đ Í Ó Ư, số).
- Nếu từng chơi các bản dịch thử nghiệm trước tháng 9/2026, thú trong save cũ
  có thể mang chỉ số bị lỗi; nên nuôi vườn mới để chơi ổn định.

## Bản quyền

Trò chơi, tên gọi và hình ảnh thuộc Konami và các chủ sở hữu liên quan. Bản vá
chỉ chứa phần chữ dịch, phông chữ vẽ lại và vài byte mã điều chỉnh; không phân
phối dữ liệu gốc. Nếu chủ sở hữu bản quyền yêu cầu, bản vá sẽ được gỡ.
