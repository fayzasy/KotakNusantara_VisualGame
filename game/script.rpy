# ==============================================================
# GAME SCRIPT - WIRA'S JOURNEY
# Struktur: Opening → CP1 Minangkabau → CP2 → CP3 → CP4 → CP5 → Ending
# ==============================================================


# ==============================================================
# SECTION 1: CHARACTER DEFINITIONS
# ==============================================================

define narrator    = Character("",            who_color="#ffffff")
define wira        = Character("Wira",        who_color="#ffffff")
define nenek       = Character("Nenek",       who_color="#ffffff")
define ibu         = Character("Ibu",         who_color="#ffffff")
define ayah        = Character("Ayah",        who_color="#ffffff")
define garuda      = Character("Garuda",      who_color="#ffffff")
define Datuak      = Character("Datuak",      who_color="#ffffff")
define Buya_Hamid  = Character("Buya Hamid",  who_color="#ffffff")
define Dr_Sari     = Character("Dr Sari",     who_color="#ffffff")
define Rosma       = Character("Ibu Rosma",   who_color="#ffffff")
define Amelia      = Character("Amelia",      who_color="#ffffff")
define Rizky       = Character("Rizky",       who_color="#ffffff")


# ==============================================================
# SECTION 2: SISTEM POIN
# ==============================================================

default player_points = 0


# ==============================================================
# SECTION 3: IMAGE DEFINITIONS
# ==============================================================

# --- UMUM ---
image black = "black-bg.jpg"

# --- PROLOG: TERAS PAGI ---
image bg_prolog_teras_pagi  = "prolog_teras_pagi.png"
image wira_ceria             = "wira_ceria.png"
image pipit_standing         = "pipit_standing.png"
image pipit_terbang          = "pipit_terbang.png"
image wiranpipit             = "wira_dan_pipit.png"
image wiranpipit_serius      = "wira_dan_pipit_serius.png"
image wiranpipit_nunduk      = "wira_dan_pipit_nunduk.png"
image wiranpipit_terharu     = "wira_dan_pipit_terharu.png"

# --- PROLOG: TAMAN KOTA SORE ---
image taman                  = im.Scale("prolog_taman_kota_sore.png", 1920, 1080)
image wira_megang_sangkar    = "wira_megang_sangkar.png"
image wira_duduk_sangkar     = "wira_duduk_sangkar.png"
image wira_ketiup_angin      = "Wira ketiup angin kenceng.png"
image pipit_hinggap_sangkar  = "pipit hinggap di sangkar.png"
image wira_ngejar            = "wira_ngejar.png"
image sangkar                = "sangkar.png"
image wira_sedih             = "wira sedih.png"

# --- PROLOG: KAMAR WIRA ---
image kamarwira              = "prolog_kamar_wira.png"
image wira_sinis             = "wira dewasa sinis.png"
image wira_bingung           = "wira dewasa bingung.png"

# --- CP1 MINANGKABAU: KARAKTER ---
image rumah_gadang           = im.Scale("rumah_gadang.png", 1920, 1080)
image garuda_berdiri         = "garuda_default.png"
image garuda_berbicara       = "garuda_bicara.png"
image garuda_ceria           = "garuda_ceria.png"
image wira_tunjuk            = "wira_tunjuk2.png"

# --- CP1 MINANGKABAU: BACKGROUND ---
image bg_misi                = im.Scale("dalam_gadang.png", 1920, 1080)
image forum                  = im.Scale("forum.png", 1920, 1080)
image forum2                 = im.Scale("forum_2.png", 1920, 1080)
image forum3                 = im.Scale("forum_3.png", 1920, 1080)
image forum4                 = im.Scale("forum_4.png", 1920, 1080)
image forum5                 = im.Scale("forum_5.png", 1920, 1080)
image bingungsemua           = im.Scale("forum_bingung.png", 1920, 1080)
image bg_balai               = im.Scale("bg_balai.png", 1920, 1080)
image saling_kecewa          = im.Scale("saling_kecewa.png", 1920, 1080)

# --- CP1 MINANGKABAU: SCENE PILIHAN BALAI ADAT ---
image pilihan_a              = im.Scale("pilihan_a.png", 1920, 1080)
image pilihan_b              = im.Scale("pilihan_b.png", 1920, 1080)
image pilihan_c              = im.Scale("pilihan_c.png", 1920, 1080)

# --- CP1 MINANGKABAU: SCENE RUMAH GADANG ---
image openingscene_rumahgadang    = im.Scale("openingscene_rumahgadang.png", 1920, 1080)
image aset_pilihana_rumahgadang   = im.Scale("aset_pilihana_rumahgadang.png", 1920, 1080)
image aset_pilihanb_rumahgadang   = im.Scale("aset_pilihanb_rumahgadang.png", 1920, 1080)
image aset_pilihanc_rumahgadang   = im.Scale("aset_pilihanc_rumahgadang.png", 1920, 1080)
image rosma_khawatir              = im.Scale("rosma_khawatir.png", 1920, 1080)
image percakapan_awal_rumahgadang = im.Scale("percakapan_awal_rumahgadang.png", 1920, 1080)
image rumahgadang_c_solved        = im.Scale("rumahgadang_c_solved.png", 1920, 1080)

# --- CP1 MINANGKABAU: SCENE PASAR ---
image visual_awal_scenepasar      = im.Scale("visual_awal_scenepasar.png", 1920, 1080)
image percakapan_awal_scenepasar  = im.Scale("percakapan_awal_scenepasar.png", 1920, 1080)
image perdebatanpanas_pasar       = im.Scale("perdebatanpanas_pasar.png", 1920, 1080)
image pasar_a_solved              = im.Scale("pasar_a_solved.png", 1920, 1080)
image pasar_c_solved              = im.Scale("pasar_c_solved.png", 1920, 1080)

# --- CP1 MINANGKABAU: PILIHAN BUTTON ASET ---
image misi_balaiadat         = "balai_adat_only.png"
image misi_rumahgadang       = "rumah_gadang_only.png"
image misi_pasar             = "pasar_only.png"
image peta_penuh             = "peta_penuh.png"
image poin_rendah            = im.Scale("poin_rendah.png", 1920, 1080)
image poin_sedang            = im.Scale("poin_sedang.png", 1920, 1080)
image poin_tinggi            = im.Scale("poin_tinggi.png", 1920, 1080)

# Sirih buttons (Balai Adat)
image sirih1_idle  = "sirih1_idle.png"
image sirih1_hover = "sirih1_hover.png"
image sirih2_idle  = "sirih2_idle.png"
image sirih2_hover = "sirih2_hover.png"
image sirih3_idle  = "sirih3_idle.png"
image sirih3_hover = "sirih3_hover.png"

# Rumah Gadang buttons
image rumahgadang_a_idle  = "rumahgadang_a_idle.png"
image rumahgadang_a_hover = "rumahgadang_a_hover.png"
image rumahgadang_b_idle  = "rumahgadang_b_idle.png"
image rumahgadang_b_hover = "rumahgadang_b_hover.png"
image rumahgadang_c_idle  = "rumahgadang_c_idle.png"
image rumahgadang_c_hover = "rumahgadang_c_hover.png"

# Pasar buttons
image pasar_a_idle  = im.Scale("pasar_a_idle.png", 700, 800)
image pasar_a_hover = im.Scale("pasar_a_hover.png", 700, 800)
image pasar_b_idle  = im.Scale("pasar_b_idle.png", 700, 800)
image pasar_b_hover = im.Scale("pasar_b_hover.png", 700, 800)
image pasar_c_idle  = im.Scale("pasar_c_idle.png", 700, 800)
image pasar_c_hover = im.Scale("pasar_c_hover.png", 700, 800)

# --- CP2 - CP5: Tambahkan image definitions di sini ---
# image cp2_bg_xxx = im.Scale("xxx.png", 1920, 1080)
# image cp3_bg_xxx = im.Scale("xxx.png", 1920, 1080)
# dst...


# ==============================================================
# SECTION 4: TRANSFORM DEFINITIONS
# ==============================================================

transform pipit_initial:
    xalign 0.4
    yalign 0.495
    zoom 0.13

transform wleft_small:
    xalign 0.23
    yalign 0.65
    zoom 0.6

transform wright_small:
    xalign 0.77
    yalign 0.65
    zoom 0.6

transform wcenter_small:
    xalign 0.5
    yalign 0.5
    zoom 0.6

transform teras:
    xalign 0.5
    yalign 0.72
    zoom 0.6

transform terasnew:
    xalign 0.5
    yalign 0.72
    zoom 0.65

transform wira_megang_sangkar_t:
    xalign 0.35
    yalign 0.6
    zoom 0.3

transform wira_duduk_sangkar_t:
    xalign 0.38
    yalign 0.6
    zoom 0.3

transform wira_ketiup_angin_t:
    xalign 0.42
    yalign 0.6
    zoom 0.3

transform wira_sedih_t:
    xalign 0.42
    yalign 0.6
    zoom 0.4

transform pipit_sangkar:
    xalign 0.32
    yalign 0.67
    zoom 0.3

transform pipit_terbang_t:
    xalign 0.2
    yalign 0.3
    zoom 0.2

transform pipit_leaving:
    xalign 0
    yalign 0
    zoom 0.2

transform sangkar_kosong:
    xalign 0.34
    yalign 0.64
    zoom 0.2

transform atas_sangkar:
    xalign 0.34
    yalign 0.6
    zoom 0.15

transform chara_wira_sinis:
    xalign 0.7
    yalign 1.0


# ==============================================================
# SECTION 5: SCREEN DEFINITIONS
# ==============================================================

# ---- Screen: Tampilan Poin (muncul di sudut kanan atas) ----
screen show_points():
    vbox:
        xalign 0.95
        yalign 0.05
        spacing 10
        text "POIN: [player_points]":
            size 28
            color "#FFD700"
            text_align 1.0

# ---- Screen: Pilihan Balai Adat (Sirih) ----
screen pilihan_sirih():
    modal True
    default hovered = None
    hbox:
        spacing 80
        xalign 0.5
        yalign 0.75
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "sirih1_idle.png"
                hover "sirih1_hover.png"
                action Jump("pilihan_a")
                hovered SetScreenVariable("hovered", "A")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN A\nMENDENGARKAN\nSEMUA UNSUR":
                xalign 0.5
                size 22
                text_align 0.5
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "sirih2_idle.png"
                hover "sirih2_hover.png"
                action Jump("pilihan_b")
                hovered SetScreenVariable("hovered", "B")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN B\nHANYA\nTETUA":
                xalign 0.5
                size 22
                text_align 0.5
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "sirih3_idle.png"
                hover "sirih3_hover.png"
                action Jump("pilihan_c")
                hovered SetScreenVariable("hovered", "C")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN C\nMENGABAIKAN\nFORUM":
                xalign 0.5
                size 22
                text_align 0.5

# ---- Screen: Pilihan Rumah Gadang ----
screen pilihan_rumahgadang():
    modal True
    default hovered = None
    hbox:
        spacing 80
        xalign 0.5
        yalign 0.75
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "rumahgadang_a_idle.png"
                hover "rumahgadang_a_hover.png"
                action Jump("pilihan_rumahgadang_a")
                hovered SetScreenVariable("hovered", "A")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN A":
                xalign 0.5
                size 22
                text_align 0.5
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "rumahgadang_b_idle.png"
                hover "rumahgadang_b_hover.png"
                action Jump("pilihan_rumahgadang_b")
                hovered SetScreenVariable("hovered", "B")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN B":
                xalign 0.5
                size 22
                text_align 0.5
        vbox:
            xalign 0.5
            spacing 10
            imagebutton:
                idle "rumahgadang_c_idle.png"
                hover "rumahgadang_c_hover.png"
                action Jump("pilihan_rumahgadang_c")
                hovered SetScreenVariable("hovered", "C")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN C":
                xalign 0.5
                size 22
                text_align 0.5

# ---- Screen: Pilihan Pasar ----
screen pilihan_pasar():
    modal True
    default hovered = None
    hbox:
        spacing 60
        xalign 0.5
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            imagebutton:
                idle "pasar_a_idle"
                hover "pasar_a_hover"
                action Jump("pilihan_pasar_a")
                hovered SetScreenVariable("hovered", "A")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN A":
                xalign 0.5
                size 20
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            imagebutton:
                idle "pasar_b_idle"
                hover "pasar_b_hover"
                action Jump("pilihan_pasar_b")
                hovered SetScreenVariable("hovered", "B")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN B":
                xalign 0.5
                size 20
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            imagebutton:
                idle "pasar_c_idle"
                hover "pasar_c_hover"
                action Jump("pilihan_pasar_c")
                hovered SetScreenVariable("hovered", "C")
                unhovered SetScreenVariable("hovered", None)
            text "PILIHAN C":
                xalign 0.5
                size 20

# ---- Screen: Pilihan CP2 (template, ganti sesuai kebutuhan) ----
# screen pilihan_cp2():
#     ...

# ---- Screen: Pilihan CP3 ----
# screen pilihan_cp3():
#     ...

# ---- Screen: Pilihan CP4 ----
# screen pilihan_cp4():
#     ...

# ---- Screen: Pilihan CP5 ----
# screen pilihan_cp5():
#     ...


# ==============================================================
# SECTION 6: GAME FLOW - OPENING
# ==============================================================

label start:

    # ============================================================
    # OPENING 1 - TERAS PAGI
    # ============================================================
    scene bg_prolog_teras_pagi
    show pipit_standing as pipit at pipit_initial
    with fade

    narrator "Pada suatu hari..."
    show wira_ceria as wira at wleft_small
    with dissolve

    wira "Wah... hari ini cerah sekali ya!"

    window hide
    show wira_ceria as wira at teras
    with ease
    pause 0.5
    window show
    wira "Pipit... lihat deh. Matahari pagi ini bagus banget, kan?"

    window hide
    pause 0.3
    show pipit_terbang as pipit at pipit_initial
    with dissolve
    pause 0.5

    hide pipit        
    scene bg_prolog_teras_pagi
    hide wira
    show wiranpipit as wira at teras
    with dissolve
    window show

    narrator "Wira terkekeh geli, matanya semakin berbinar."
    wira "Ih, geli! Kamu suka ya aku elus-elus?"
    narrator "Bagi Wira, dunia luar penuh dengan suara bising dan kebingungan. Namun, di teras ini, bersama Pipit... semuanya terasa benar."

    window hide
    show wiranpipit_serius as wira at teras
    with dissolve
    pause 0.5
    window show

    wira "Pipit... kalau nanti sayapmu sudah kuat... kalau kamu sudah bisa terbang jauh sampai ke awan..."

    window hide
    show wiranpipit_nunduk as wira at terasnew
    with dissolve
    pause 1.5
    show wiranpipit_terharu as wira at teras
    with dissolve
    pause 1.5
    window show

    wira "...jangan tinggalin aku ya? Janji?"
    narrator "Di teras rumah itu, Wira kecil mengunci separuh hatinya pada seekor burung peliharaan, menjadikannya satu-satunya dunia kecil yang dia miliki."
    window hide

    # ============================================================
    # OPENING 2 - TAMAN KOTA SORE
    # ============================================================
    scene taman
    with dissolve

    show wira_megang_sangkar as wira at wira_megang_sangkar_t
    with dissolve
    pause 1.0
    window show
    wira "Kita sudah sampai, Pipit! Lihat, di sini jauh lebih luas daripada kamar aku."
    window hide
    pause 0.5

    hide wira
    show wira_duduk_sangkar as wira at wira_duduk_sangkar_t
    with dissolve
    pause 1.0
    window show
    wira "Aku buka ya pintunya? Tapi kamu jangan terbang tinggi-tinggi... aku takut nggak bisa liat kamu lagi."
    wira "Ayo... keluar sebentar..."
    window hide
    pause 0.5

    hide wira
    show wira_ketiup_angin as wira at wira_ketiup_angin_t
    show pipit_hinggap_sangkar as pipit at pipit_sangkar
    with dissolve
    pause 1.0
    window show
    wira "Pipit?! Tunggu!"
    window hide
    pause 0.5

    hide pipit
    hide wira
    show sangkar at sangkar_kosong
    show wira_ngejar as wira at wira_ketiup_angin_t
    show pipit_terbang as pipit at atas_sangkar
    with dissolve
    pause 0.5

    show pipit_terbang as pipit at pipit_leaving
    with ease
    hide pipit
    pause 0.5

    window show
    wira "JANGAN TINGGALIN AKU! PIPIT!!!"
    pause 1.0
    window hide

    scene taman
    show wira_sedih as wira at wira_ketiup_angin_t
    with dissolve
    pause 2.0

    scene black
    with dissolve
    narrator "...."
    narrator "Pipit terbang.... entah kemana..."

    # ============================================================
    # OPENING 3 - KAMAR WIRA (tidak perlu diubah, sudah rapi)
    # ============================================================
    scene kamarwira
    with dissolve
    show wira_sinis as wira at chara_wira_sinis
    narrator "(Telepon berdering)"
    show wira_bingung as wira at chara_wira_sinis
    with dissolve
    wira "Halo?"
    ibu "Wira, besok kamu ke desa Nenek ya. Sudah Ibu siapkan semuanya."
    show wira_sinis as wira at chara_wira_sinis
    with dissolve
    wira "Ma, aku bukan anak kecil lagi yang bisa disuruh-suruh ke desa nggak jelas gitu. Males."
    ayah "Wira! Turuti kata Ibu! Kamu terlalu banyak membuang waktu dengan hal-hal nggak berguna di sana."
    ayah "Kalau besok kamu tidak berangkat, Papa potong uang jajan dan sita semua peralatan game mu!"
    show wira_bingung as wira at chara_wira_sinis
    wira "Apa-apaan sih? Kok jadi ngancem gitu?!"
    ibu "Ini untuk kebaikanmu, Sayang. Besok berangkat ya. Dadah!"
    wira "Males deh, selalu aja kayak gini."

    jump cp1_minangkabau_intro


# ==============================================================
# SECTION 7: CHECKPOINT 1 - MINANGKABAU
# ==============================================================

label cp1_minangkabau_intro:

    scene black
    scene rumah_gadang
    with dissolve

    show wira_bingung at wleft_small
    with dissolve

    wira "Itu... rumahnya kok atapnya kayak tanduk kerbau gitu?"
    wira "Bangunannya gede banget! Tapi kelihatannya udah lama nggak dirawat."

    window hide
    show garuda_berdiri at wright_small
    with dissolve
    pause 0.5
    window show
    hide wira_bingung

    garuda "Selamat datang di Nagari Minangkabau, Wira!"
    hide garuda_berdiri

    show wira_bingung at wleft_small
    with dissolve
    wira "Nagari? Ini semacam desa ya?"
    hide wira_bingung

    show garuda_berbicara at wright_small

    garuda "Lebih dari itu. Nagari adalah unit kehidupan masyarakat Minangkabau."
    garuda "Tempat adat dijalankan, keputusan diambil bersama, dan identitas dijaga turun-temurun."
    garuda "Rumah Gadang yang kamu lihat itu... adalah jantungnya."
    hide garuda_berbicara

    show wira_tunjuk at wleft_small
    with dissolve
    wira "Jantungnya? Kelihatan sudah mau roboh di sudut sana."
    hide wira_tunjuk

    show garuda_ceria at wcenter_small
    garuda "Tepat sekali! Itulah kenapa kamu ada di sini."

    # Penjelasan misi oleh Garuda
    window hide
    scene black
    scene bg_misi
    with dissolve
    window show
    show garuda_berbicara at wright_small

    garuda "Inilah misimu di Minangkabau, Wira. Nagari ini sedang di persimpangan. Terdapat tiga krisis yang harus kamu hadapi."
    hide garuda_berbicara

    show wira_bingung at wleft_small
    with dissolve
    wira "Tiga?"
    window hide
    hide wira_bingung

    show misi_balaiadat at wcenter_small
    with dissolve
    pause 0.5
    window show
    garuda "Pertama — forum musyawarah adat hampir lumpuh karena para tokoh tidak bisa mencapai kata sepakat."

    hide misi_balaiadat
    show misi_rumahgadang at wcenter_small
    with dissolve
    pause 0.5
    garuda "Kedua — Rumah Gadang warisan leluhur terancam diubah tampilannya tanpa pertimbangan adat."

    hide misi_rumahgadang
    show misi_pasar at wcenter_small
    with dissolve
    pause 0.5
    garuda "Ketiga — ada tawaran bisnis menggiurkan yang berbenturan keras dengan nilai adat dan agama."

    hide misi_pasar
    show garuda_berbicara at wcenter_small
    with dissolve
    pause 0.5
    garuda "Ingat — setiap pilihanmu akan mencerminkan siapa dirimu sebenarnya."
    window hide

    # Perkenalan 4 pilar nagari
    scene forum
    with dissolve
    window show
    garuda "Perkenalkan empat pilar nagari."
    garuda "Datuak Rajo Nan Sati, Niniak Mamak, penjaga garis keturunan dan hukum adat."
    garuda "Buya Hamid, Alim Ulama, penjaga syariat Islam dalam kehidupan masyarakat."
    garuda "Dr. Sari Rahmawati, Cadiak Pandai, kaum intelektual yang membawa pengetahuan dunia luar."
    garuda "Ibu Rosma, Bundo Kanduang, simbol kebijaksanaan perempuan dalam nagari."

    wira "Kok mereka kelihatan kayak mau berantem?"
    garuda "Karena mereka sedang berselisih soal satu keputusan besar dan suara mereka tidak bulat."

    scene forum2
    with dissolve
    Datuak "Adat basandi syarak, syarak basandi Kitabullah! Segala keputusan harus lewat tangan kami, Niniak Mamak."
    Datuak "Kami yang menjaga pusaka, kami yang menentukan arah nagari!"

    scene forum3
    with dissolve
    Buya_Hamid "Benar bahwa adat bersumber pada agama. Tapi keputusan yang menyimpang dari nilai Islam tidak bisa dibenarkan hanya karena itu keputusan Niniak Mamak. Agama adalah fondasi, bukan pelengkap."

    scene forum4
    with dissolve
    Dr_Sari "Saya setuju bahwa kita harus menjaga nilai. Tapi data menunjukkan bahwa nagari yang tidak bisa beradaptasi dengan perubahan ekonomi akan ditinggal generasi mudanya. Kita tidak bisa menutup mata terhadap realita."

    scene forum5
    with dissolve
    Rosma "Anak-anak kita yang pergi merantau, mereka akan pulang jika nagari ini punya jiwa. Tanpa keselarasan antara adat, agama, dan ilmu, nagari ini hanya kulit tanpa isi."

    window hide
    scene bingungsemua
    with dissolve
    window show
    Datuak "Siapa anak muda ini?"
    garuda "Ia adalah tamu nagari yang sedang dalam perjalanan belajar. Izinkan ia mendengarkan forum ini."

    # --- Pilihan pertama: Balai Adat ---
    show bg_balai
    show screen show_points
    window hide
    call screen pilihan_sirih

# ---- Pilihan A: Mendengarkan Semua Unsur ----
label pilihan_a:
    scene pilihan_a
    with dissolve
    window show

    narrator "Wira duduk tenang di sudut ruangan, mendengarkan satu per satu pendapat semua tokoh dengan seksama, tidak menyela, dan mencatat dalam ingatannya sebelum mengambil kesimpulan apa pun."
    pause 1.0

    scene forum2
    with dissolve
    Datuak "Anak muda ini... ia mendengar dengan benar."

    pause 0.5
    scene forum5
    with dissolve
    Rosma "Mendengarkan semua suara sebelum berbicara... itu kebijaksanaan."

    pause 0.5
    scene black
    with dissolve
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Kamu baru saja memahami inti dari musyawarah mufakat. Kebenaran tidak dimiliki satu pihak saja. Ia lahir dari pertemuan berbagai sudut pandang."

    window hide
    pause 1.0
    window show

    $ player_points += 20
    hide garuda_berbicara
    narrator "Anda mendapat 20 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis

# ---- Pilihan B: Hanya Mendengarkan Tetua ----
label pilihan_b:
    scene pilihan_b
    with dissolve
    window show

    narrator "Wira fokus pada perkataan Datuak Rajo Nan Sati saja karena dianggap paling senior, mengabaikan pendapat tokoh lainnya."
    pause 1.0
    pause 1.0

    window hide
    scene bingungsemua
    with dissolve
    window show

    narrator "Buya Hamid, Dr. Sari, dan Ibu Rosma menyadari Wira hanya memperhatikan Datuak. Ketiganya saling berpandangan dengan ekspresi kecewa."

    pause 0.5
    scene saling_kecewa
    with dissolve
    Dr_Sari "Sayangnya, generasi muda masih berpikir bahwa usia yang menentukan kebenaran."

    pause 0.5
    scene black
    with dissolve
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Adat Minangkabau bukan hierarki buta, Wira. Ia adalah harmoni. Ketika kamu memilih untuk hanya mendengar satu suara, kamu merusak keseimbangan yang dibangun berabad-abad."

    window hide
    pause 1.0
    window show

    $ player_points -= 10
    narrator "Anda kehilangan 10 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis

# ---- Pilihan C: Mengabaikan Forum ----
label pilihan_c:
    scene pilihan_c
    with dissolve
    window show

    narrator "Wira merasa forum ini membosankan, ia berdiri di sudut sambil bermain-main memperhatikan ukiran dinding."
    narrator "Suasana forum semakin tegang. Semua tokoh semakin keras mempertahankan posisinya."
    pause 1.0

    window hide
    scene bingungsemua
    with dissolve
    window show

    Datuak "Anak muda ini... tidak menghargai musyawarah adat kami!"
    Buya_Hamid "Ia bahkan tidak mencoba memahami kompleksitas masalah ini!"

    scene black
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Wira... kehadiranmu di ruangan ini punya arti. Ketika kamu memilih untuk tidak hadir sepenuhnya, kamu membiarkan konflik tumbuh tanpa ada yang mau memahami semua sisi."

    window hide
    pause 1.0
    window show

    $ player_points -= 20
    narrator "Anda kehilangan 20 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis

# ---- Scene: Krisis Rumah Gadang ----
label scene_rumahgadang_krisis:
    scene black
    with fade

    window hide
    pause 1.0

    scene openingscene_rumahgadang
    with dissolve
    window show

    Amelia "Pak Rizky, saya setuju dindingnya harus diperbaiki. Tapi saya rasa kita bisa sekalian renovasi total. Tambah kaca panoramik di sisi timur, ganti material atap dengan bahan modern yang lebih tahan lama, dan buat interior yang lebih minimalis. Lebih estetik dan fungsional!"
    Rizky "Secara teknis bisa dan lebih efisien biayanya dibanding restorasi ukiran lama satu per satu."
    pause 1.0

    scene rosma_khawatir
    with dissolve
    window show
    Rosma "Amelia... yang kamu bicarakan itu bukan renovasi. Itu penggantian jiwa rumah ini."

    scene percakapan_awal_rumahgadang
    Amelia "Tapi bu, struktur bangunannya sudah tidak aman! Kalau tidak diperbaiki sekarang, bisa roboh. Lebih baik diperbarui daripada dibiarkan rusak."
    Rosma "Setiap ukiran di dinding itu punya nama. Punya cerita. Kalau diganti dengan kaca dan beton, yang tersisa hanya bentuknya saja. Bukan rohnya."
    garuda "Rumah Gadang bukan sekadar bangunan, Wira. Ia adalah silsilah keluarga yang tertulis dalam kayu. Setiap ruangan mencerminkan posisi perempuan sebagai pemegang harta pusaka. Setiap ukiran adalah bahasa yang berbicara tentang falsafah hidup."
    wira "Tapi kalau memang sudah mau roboh...?"
    garuda "Tepat sekali pertanyaannya. Di sinilah keputusanmu diuji."

    pause 1.0

    show openingscene_rumahgadang
    show screen show_points
    window hide
    call screen pilihan_rumahgadang

# ---- Pilihan Rumah Gadang A: Restorasi Tradisional ----
label pilihan_rumahgadang_a:
    scene aset_pilihana_rumahgadang
    with dissolve
    window show

    narrator "Wira memilih untuk mempertahankan struktur asli Rumah Gadang sambil melakukan restorasi yang menghormati tradisi."
    pause 1.0

    Rosma "Anak ini... mengerti bahwa warisan bukan beban. Warisan adalah identitas."
    Amelia "Mungkin, saya terlalu fokus pada yang rusak, sampai lupa apa yang masih utuh dan berharga. Baiklah, kita cari ahli restorasi."
    garuda "Kamu baru saja memahami bahwa menjaga identitas budaya bukan berarti menolak perubahan. Ini berarti memastikan perubahan tidak menghapus siapa kita."

    window hide
    pause 1.0
    window show

    $ player_points += 25
    narrator "Anda mendapat 25 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

# ---- Pilihan Rumah Gadang B: Jalan Tengah ----
label pilihan_rumahgadang_b:
    scene aset_pilihanb_rumahgadang
    with dissolve
    window show

    wira "Mungkin bisa diambil jalan tengah? Bagian yang lapuk diganti material modern, tetapi ukirannya tetap dipertahankan. Jadi lebih aman tetapi masih ada nuansa tradisionalnya."
    garuda "Niatmu baik, Wira. Tapi jalan tengah yang tidak dipikirkan matang bisa menjadi solusi yang tidak memuaskan semua pihak. Warisan budaya butuh perlindungan penuh, bukan kompromi setengah hati."

    window hide
    pause 1.0
    window show

    $ player_points += 10
    narrator "Anda mendapat 10 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

# ---- Pilihan Rumah Gadang C: Renovasi Modern ----
label pilihan_rumahgadang_c:
    scene aset_pilihanc_rumahgadang
    with dissolve
    window show

    wira "Saya setuju dengan Amelia. Yang penting bangunannya aman dan fungsional. Bentuknya bisa disesuaikan dengan kebutuhan zaman."

    pause 1.0
    scene rumahgadang_c_solved
    garuda "Wira... kamu baru saja memilih kenyamanan sesaat. Ketika Rumah Gadang kehilangan ukirannya, generasi berikutnya tidak akan tahu dari mana mereka berasal."

    window hide
    pause 1.0
    window show

    $ player_points -= 25
    narrator "Anda kehilangan 25 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

# ---- Scene: Krisis Pasar ----
label scene_pasar_krisis:
    scene black
    with fade

    window hide
    pause 1.0

    scene visual_awal_scenepasar
    with dissolve
    window show

    narrator "Setelah mengatasi situasi Rumah Gadang, Garuda membawa Wira ke pasar nagari. Suasana begitu ramai dan hidup..."
    pause 1.0

    show garuda_berbicara at wcenter_small
    with dissolve

    garuda "Ini adalah tantangan terakhir, Wira. Sebuah perusahaan besar dari kota menawarkan investasi besar untuk nagari."
    pause 0.5
    garuda "Tapi ada yang janggal. Mereka ingin mengubah cara hidup masyarakat di sini. Semua orang menjadi bingung."

    hide garuda_berbicara
    pause 1.0

    narrator "Wira melihat forum impromptu di pasar. Para tokoh tengah berdebat sengit tentang penawaran ini."
    narrator "Setiap keputusan akan menentukan masa depan ekonomi nagari. Wira harus memilih dengan bijak."
    pause 1.0

    show visual_awal_scenepasar
    show screen show_points
    call screen pilihan_pasar

# ---- Pilihan Pasar A: Tolak dengan Berprinsip ----
label pilihan_pasar_a:
    scene percakapan_awal_scenepasar
    with dissolve
    window show

    wira "Pak Harlan, saya ngerti tawaran ini menarik secara ekonomi. Tapi nagari ini punya fondasi yang tidak bisa dikompromikan. Kalau investasinya memang ingin membantu nagari, bisa diajukan format yang sesuai dengan nilai Islam dan adat."
    wira "Kerja sama yang benar-benar saling menguntungkan, bukan yang merusak dari dalam."
    pause 1.0

    scene pasar_a_solved
    with dissolve
    window show
    narrator "Harlan terdiam dan melangkah pergi."
    Datuak "Anak muda ini... berbicara dengan lidah orang berprinsip. Jarang ada yang berani menolak uang dengan cara yang terhormat seperti itu."
    Buya_Hamid "Kekayaan yang dibangun di atas kerusakan akhlak bukan kemakmuran. Itu bencana yang tertunda."
    garuda "Kamu baru saja memahami sesuatu yang paling sulit — bahwa integritas adalah pilihan aktif, bukan kondisi pasif, dan paling keras diuji ketika godaannya paling besar."

    window hide
    pause 1.0
    window show

    $ player_points += 30
    narrator "Anda mendapat 30 poin! Total poin: [player_points]"

    jump ending_minangkabau

# ---- Pilihan Pasar B: Ragu-ragu ----
label pilihan_pasar_b:
    scene perdebatanpanas_pasar
    with dissolve
    window show

    wira "Hmm... ini susah ya. Dua-duanya ada benarnya. Mungkin bisa dikaji lebih lanjut lagi."
    pause 1.0

    garuda "Diam di antara yang benar dan salah, Wira, bukan kebijaksanaan. Itu kebimbangan yang membiarkan yang salah berjalan terus. Kadang, keberanian terbesar adalah berani mengambil sikap."

    window hide
    pause 1.0
    window show

    $ player_points -= 5
    narrator "Anda kehilangan 5 poin! Total poin: [player_points]"

    jump ending_minangkabau

# ---- Pilihan Pasar C: Setuju Investasi ----
label pilihan_pasar_c:
    scene pasar_c_solved
    with dissolve
    window show

    garuda "Wira... kamu baru saja memvalidasi penghancuran fondasi sebuah nagari dengan tangan kamu sendiri."
    garuda "Nagari yang kehilangan prinsipnya bukan lagi nagari yang sama. Ia hanya nama tanpa jiwa."
    pause 0.5

    $ player_points -= 30
    narrator "Anda kehilangan 30 poin! Total poin: [player_points]"

    jump ending_minangkabau

# ---- Ending CP1: Minangkabau ----
label ending_minangkabau:
    scene black
    with fade

    window hide
    pause 1.5

    show garuda_berbicara at wcenter_small
    with dissolve
    window show

    if player_points >= 65:
        hide garuda_berbicara
        scene poin_tinggi
        with dissolve
        garuda "Kamu mulai memahami bahwa demokrasi yang sesungguhnya bukan tentang suara terbanyak. Ini tentang keselarasan semua unsur — dan bahwa prinsip bukan penghalang kemajuan, ini adalah kompas yang memastikan kita tidak tersesat di tengah perjalanan."

    elif player_points >= 25:
        hide garuda_berbicara
        scene poin_sedang
        with dissolve
        garuda "Ada momen di mana kamu membuka matamu dan momen di mana kamu masih memilih jalan yang mudah. Nagari ini mengajarkan bahwa setengah hadir lebih berbahaya dari tidak hadir sama sekali."

    else:
        hide garuda_berbicara
        scene poin_rendah
        with dissolve
        garuda "Wira... di setiap pilihan yang kamu anggap pragmatis, kamu sebenarnya sedang membiarkan sesuatu yang orang lain jaga dengan nyawa mereka selama berabad-abad runtuh perlahan. Adat bukan museum."

    window hide
    pause 2.0

    jump cp2_intro  # Lanjut ke Checkpoint 2


# ==============================================================
# SECTION 8: CHECKPOINT 2 - [NAMA LOKASI / BUDAYA]
# ==============================================================
# Poin carry over dari CP1.
# Struktur sama: intro → perkenalan masalah → 1-3 pilihan → jump ke CP3

label cp2_intro:
    # TODO: Isi scene intro CP2 di sini
    # scene cp2_bg_xxx
    # with dissolve
    # ...
    # jump scene_cp2_krisis

    narrator "(CP2 belum diisi)"
    jump cp3_intro


# ==============================================================
# SECTION 9: CHECKPOINT 3 - [NAMA LOKASI / BUDAYA]
# ==============================================================

label cp3_intro:
    # TODO: Isi scene intro CP3 di sini

    narrator "(CP3 belum diisi)"
    jump cp4_intro


# ==============================================================
# SECTION 10: CHECKPOINT 4 - [NAMA LOKASI / BUDAYA]
# ==============================================================

label cp4_intro:
    # TODO: Isi scene intro CP4 di sini

    narrator "(CP4 belum diisi)"
    jump cp5_intro


# ==============================================================
# SECTION 11: CHECKPOINT 5 - [NAMA LOKASI / BUDAYA]
# ==============================================================

label cp5_intro:
    # TODO: Isi scene intro CP5 di sini

    narrator "(CP5 belum diisi)"
    jump ending_final


# ==============================================================
# SECTION 11: ENDING FINAL
# ==============================================================

label ending_final:

    scene black
    with fade
    window hide
    pause 1.5

    if player_points >= 120:
        jump closing_good_ending
    else:
        jump closing_bad_ending

# ==============================================================
# GOOD ENDING
# ==============================================================

label closing_good_ending:

    # --- Scene 1: Teras Rumah Nenek ---
    scene black
    with dissolve
    pause 0.5

    scene closing_good_teras
    with dissolve

    window show
    narrator "Wira membuka mata."
    narrator "Pemandangan pertama yang ia tangkap adalah teras rumah nenek — tapi kali ini berbeda dari yang ia ingat."
    narrator "Pagar kayu yang dulu keropos sudah diganti. Bunga-bunga tumbuh di pot tanah liat. Anak-anak berlarian di jalan."
    window hide

    pause 1.0

    play sound "suara_kampung_hangat.ogg"    # suara percakapan warga + tawa anak-anak

    window show
    narrator "Suara tawa anak-anak mengalir dari ujung gang. Seseorang menyapa tetangganya. Ada yang berbagi makanan di teras sebelah."
    window hide

    pause 1.0

    # Nenek masuk
    show nenek_duduk at wright_small
    with dissolve
    window show

    nenek "Nak Wira... sudah bangun? Nenek buatkan teh manis pakai jahe. Dingin-dingin begini enak."

    show wira_dewasa_senyum at wleft_small
    with dissolve

    wira "Iya, Nek. Makasih."

    # --- Scene 2: Minum Teh Bersama ---
    scene closing_good_minum_teh
    with dissolve
    window show

    wira "Nek... kampung kita... kok sekarang jadi lebih… hidup?"

    nenek "Hidup? Memang pernah mati?"

    wira "Bukan gitu, Nek. Maksud aku... dulu kayaknya sepi. Sekarang jadi lebih rame. Orang-orang kayak... lebih peduli sama satu sama lain."

    nenek "Mungkin... karena ada yang belajar sesuatu dari perjalanannya. Dan bawa pulang pelajaran itu."

    window hide

    show wira_dewasa_senyum at wleft_small
    with dissolve
    pause 1.0

    window show
    narrator "Wira terdiam. Dia merasa neneknya tahu lebih dari yang dia kira."
    window hide

    # --- Scene 3: Taman Belakang, Pipit Datang ---
    scene closing_good_taman
    with dissolve
    pause 1.0

    stop sound fadeout 1.0
    play sound "suara_burung_pipit.ogg"    # suara kicauan + angin

    window show
    narrator "Wira duduk di bawah pohon besar di taman belakang rumah nenek."
    narrator "Seekor burung pipit kecil hinggap di dekatnya — mematuk-matuk sisa roti yang jatuh di tanah."
    window hide

    pause 1.0

    window show
    narrator "Suara kicauannya... familier. Persis seperti suara Garuda setiap kali memberi saran di game."
    window hide

    pause 0.5

    show wira_dewasa_terharu at wcenter_small
    with dissolve
    window show

    wira "Pipit...?"

    window hide
    pause 0.5

    # Pipit terbang ke bahu Wira
    scene closing_good_pipit_bahu
    with dissolve
    pause 1.5

    window show
    narrator "Burung itu mengepakkan sayap kecilnya. Terbang ke bahu Wira. Hinggap di sana."
    narrator "Lalu mengusapkan kepalanya pelan ke pipi Wira."
    window hide

    pause 1.5

    # --- Kilas Balik ---
    scene black
    with dissolve
    pause 0.5

    scene closing_flashback_taman           # pakai aset prolog taman yang sudah ada jika mau
    with dissolve

    window show
    narrator "Kilas balik:"
    narrator "Wira kecil menangis di taman, memegang sangkar yang sudah kosong."
    narrator "Pipit terbang ke arah matahari. Wira kecil berteriak..."
    window hide

    pause 0.5

    # Gunakan aset wira kecil dari prolog
    show wira_sedih at wcenter_small
    with dissolve
    window show

    wira "Jangan tinggalin aku!"

    window hide
    pause 1.0

    scene black
    with dissolve
    pause 0.5

    # Kembali ke taman, Pipit masih di sana
    scene closing_good_pipit_bahu
    with dissolve
    pause 1.0

    show wira_dewasa_terharu at wcenter_small
    with dissolve
    window show

    wira "Kamu... tidak pernah benar-benar pergi, ya? Kamu bahkan sampai menemani aku di dalam game itu…"

    window hide
    pause 0.5

    play sound "suara_burung_pipit.ogg"
    pause 1.0

    scene closing_good_pipit_bahu
    window show
    narrator "Burung pipit itu berkicau riang."
    narrator "Lalu terbang perlahan ke dahan pohon. Tidak pergi. Hanya hinggap di sana. Menemani."
    window hide

    pause 1.5

    # --- Zoom Out + Quote Penutup ---
    scene closing_good_zoomout
    with dissolve
    pause 2.0

    stop sound fadeout 2.0

    window show
    narrator "\"Kearifan sejati tidak hanya mendamaikan dunia luar...\""
    pause 1.0
    narrator "\"...tetapi juga mempertemukan kita kembali dengan bagian diri kita yang paling murni.\""
    window hide

    pause 2.0

    scene black
    with dissolve
    pause 1.5

    return


# ==============================================================
# BAD ENDING
# ==============================================================

label closing_bad_ending:

    # --- Scene 1: Kamar Wira, Bangun Kaget ---
    scene closing_bad_kamar
    with dissolve
    pause 0.5

    show wira_dewasa_marah at wcenter_small
    with dissolve

    play sound "suara_napas_panik.ogg"    # suara napas tidak teratur
    pause 1.5
    stop sound fadeout 1.0

    window show
    wira "Aku... gagal. Aku gagal total."
    window hide

    pause 1.0

    # --- Scene 2: Melihat dari Jendela ---
    scene closing_bad_jendela
    with dissolve
    pause 0.5

    play sound "suara_sepi_kampung.ogg"    # keheningan hampa, minim interaksi

    scene closing_bad_jalan_sepi
    with dissolve

    window show
    narrator "Di luar, kampung itu terasa asing."
    narrator "Semua orang yang berlalu-lalang memegang handphone masing-masing. Headphone di telinga. Mata tertuju ke layar. Tidak ada yang saling menyapa."
    window hide

    pause 1.5

    # Nenek jatuh, orang-orang merekam
    scene closing_bad_nenek_jatuh
    with dissolve
    pause 0.5

    window show
    narrator "Seorang nenek jatuh di halaman depan."
    narrator "Orang-orang di sekitarnya mengeluarkan HP. Merekam. Tidak ada yang bergerak untuk membantu."
    window hide

    pause 1.0

    show wira_dewasa_lelah at wcenter_small
    with dissolve
    window show

    wira "Bantu dia, dong... kenapa kalian cuma lihat?"

    window hide
    pause 1.0

    window show
    narrator "Tapi Wira sendiri tidak bergerak."
    narrator "Tangannya terpaku di kusen jendela."
    narrator "Dia baru menyadari — dia melakukan hal yang sama. Hanya melihat. Diam."
    window hide

    pause 1.5

    # --- Scene 3: Nenek Memanggil ---
    stop sound fadeout 1.0

    window show
    nenek "Wira... kamu sudah bangun? Nenek buatkan teh. Turun, ya."

    show wira_dewasa_marah at wcenter_small
    with dissolve

    wira "Gak usah! Aku gak mau teh! Aku mau sendirian!"

    window hide
    pause 0.5

    window show
    nenek "Baiklah... nanti kalau kamu mau, ambil saja di meja. Nenek taruh tehnya di meja."
    window hide

    pause 0.5

    play sound "suara_langkah_menjauh.ogg"    # langkah kaki perlahan menjauh
    pause 1.5
    stop sound fadeout 1.0

    window show
    narrator "Keheningan."
    narrator "Wira terdiam. Tangannya gemetar."
    narrator "Dia tahu dia bersikap buruk. Tapi dia tidak bisa berbuat lain. Marah adalah satu-satunya cara yang dia ketahui untuk bertahan."
    window hide

    pause 1.5

    # --- Scene 4: Di Depan Cermin ---
    scene closing_bad_cermin
    with dissolve
    pause 0.5

    show wira_dewasa_lelah at wcenter_small
    with dissolve
    pause 1.0

    window show
    narrator "Wira berdiri di depan cermin. Wajahnya lelah. Matanya merah. Kamarnya berantakan."
    window hide

    pause 1.0

    window show
    wira "Kamu... kamu egois!"
    pause 0.5
    wira "Kamu kasar! Kamu seenaknya sendiri!"
    pause 0.5
    wira "Ga heran semua orang di game benci kamu!"
    pause 0.5
    wira "Ga heran... ga heran sekarang semua orang di sini juga jadi egois."
    pause 0.5
    wira "Karena siapa? Karena kamu!"
    window hide

    pause 1.0

    # --- Scene 5: Sudut Kamar, Quote Penutup ---
    scene closing_bad_sudut_kamar
    with dissolve

    play sound "suara_ac.ogg"    # suara AC yang monoton
    pause 2.0

    window show
    narrator "\"Ketika kita memaksa dunia untuk tunduk pada keegoisan kita...\""
    pause 1.0
    narrator "\"...kita hanya akan mewariskan kehancuran — baik di tanah orang lain, maupun di rumah kita sendiri.\""
    window hide

    pause 2.0

    stop sound fadeout 2.0

    scene black
    with dissolve
    pause 1.5

    return

