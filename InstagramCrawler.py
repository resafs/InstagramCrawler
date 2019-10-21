from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time, emoji, string, csv, os, pandas as pd, pymongo
from prompt_toolkit import prompt

#Untuk ngebuat tabel awal yang ngambil isian datanya

def predictionWord(namafile):
    while 1:
        print()
        request_word = input('Masukkan kata yang bisa dimungkinkan: ')
        while len(request_word.split()) > 1:
            request_word = input('Masukkan kata yang bisa dimungkinkan hanya satu kata: ')
        connection = pymongo.MongoClient('localhost', 27017)
        db_name = connection[namafile]
        tabel = db_name[namafile+'_tabel2Mongo']
        data = tabel.find()
        data1 = tabel.find()
        save_totals = []
        hitung1 = 0        
        for row in data:
            if row['word1'] == request_word:
                save_totals.append(int(row['totals']))
            hitung1 += 1

        if len(save_totals) == 0:
            print("Maaf kata yang dicari tidak ada!")
            continue
        
        tertinggi = max(save_totals)
        print()
        hitung2 = 0
        for row in data1:
            hitung2 += 1
            if int(row['totals']) == tertinggi and row['word1'] == request_word:
                print("Kemungkinan kata yang akan dikeluarkan selanjutnya adalah '"+ str(row['word2'] +"'"))
                if hitung2 != hitung1:
                    print()
                    print('Atau')
                    print()
            if hitung2 == hitung1:
                print("Sudah itu semua kemungkinan katanya.")
                print()

            
        tanya = input('Apakah ingin mencari lagi?(y/t): ').lower()

        while tanya != 'y' and tanya != 't':
            tanya = input('Apakah ingin mencari lagi?(y/t): ').lower()
            
        if tanya == 't':
            break
        print()

def setMongo(namafile):
    setTabel1Mongo(namafile)
    setTabel2Mongo(namafile)
    setTabel3Mongo(namafile)
    setTabel4Mongo(namafile)
    setTabel5Mongo(namafile)
    setTabel6Mongo(namafile)
    print("Program Selesai!")
    
def setTabel1Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel1.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel1Mongo']
    for row in range(len(dataset)):
        username = str(dataset.loc[row, 'username'])
        caption = str(dataset.loc[row, 'caption'])
        tag = str(dataset.loc[row, 'tag'])
        likes = str(dataset.loc[row, 'likes'])
        comment = str(dataset.loc[row, 'comment'])
        data = {'username'  : 'gue', 'caption' : caption, 'tag' : tag, 'likes' : likes, 'comment': comment}
        tabel.insert_one(data)

def setTabel2Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel2.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel2Mongo']
    for row in range(len(dataset)):
        username = str(dataset.loc[row, 'id_user'])
        word1 = str(dataset.loc[row, 'word1'])
        word2 = str(dataset.loc[row, 'word2'])
        totals = str(dataset.loc[row, 'totals'])
        data = {'id_user'  : username, 'word1' : word1, 'word2' : word2, 'totals' : totals}
        tabel.insert_one(data)

def setTabel3Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel3.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel3Mongo']
    for row in range(len(dataset)):
        username = str(dataset.loc[row, 'username'])
        jml = str(dataset.loc[row, 'jumlah followers'])
        panjang = str(dataset.loc[row, 'panjang daftar followers'])
        dft = str(dataset.loc[row, 'daftar followersnya'])
        data = {'username'  : username, 'jumlah follower asli' : jml, 'jumlah follower yang diambil' : panjang, 'daftar' : dft}
        tabel.insert_one(data)

def setTabel4Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel4.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel4Mongo']
    for row in range(len(dataset)):
        username = str(dataset.loc[row, 'user sebelumnya'])
        usertarget = str(dataset.loc[row, 'usertarget'])
        jml = str(dataset.loc[row, 'jumlah followers usertarget'])
        data = {'user sebelumnya'  : username, 'usertarget' : usertarget, 'jumlah followers usertarget' : jml}
        tabel.insert_one(data)

def setTabel5Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel5.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel5Mongo']
    for row in range(len(dataset)):
        username = str(dataset.loc[row, 'commenters'])
        total = str(dataset.loc[row, 'total komen'])
        data = {'commenters'  : username, 'total komen' : total}
        tabel.insert_one(data)

def setTabel6Mongo(namafile):
    dataset = pd.read_csv(namafile+'_tabel6.csv')
    connection = pymongo.MongoClient('localhost', 27017)
    db_name = connection[namafile]
    tabel = db_name[namafile+'_tabel6Mongo']
    for row in range(len(dataset)):
        user1 = str(dataset.loc[row, 'user 1'])
        user2 = str(dataset.loc[row, 'user 2'])
        total = str(dataset.loc[row, 'total teman yang sama'])
        dft = str(dataset.loc[row, 'daftarnya'])
        data = {'user 1'  : user1, 'user 2' : user2, 'total teman yang sama' : total, 'daftarnya' : dft}
        tabel.insert_one(data)

def createAndSetTabel1(namafile,username,post,tag,likes,comment):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile)
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([username,post,tag,likes,comment])
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([username,post,tag,likes,comment])

#Untuk mengolah captionnya
def createAndSetTabel2(namafile, username, caption):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile)
        done = {}
        simpan_merge = []
        print(caption)
        for i in range(len(caption)):
            if len(caption[i]) == 1:
                caption[i].append('')
            post = caption[i]
            print(post)
            print("TIPE: " + str(type(caption)))
            split = post.split() #Untuk membuat string bisa diakses lewat index --> contoh: 'saya mau makan' akan menjadi ['saya', 'mau', 'makan']. Dipisah berdasarkan ada space atau tidak
            print(split)
            for length in range(len(split)-1):
                bantu = []
                merge = split[length] + ' ' + split[length+1]
                bantu.append(username)
                bantu.append(split[length])
                bantu.append(split[length+1])
                if bantu not in simpan_merge:
                    simpan_merge.append(bantu)
                if merge in done.keys():
                    done[merge] += 1
                else:
                    done[merge] = 1
        with open(namafile,'a',newline='') as csvfile:
            writer = csv.writer(csvfile)
            for n in range(len(simpan_merge)):
                writer.writerow([simpan_merge[n][0],simpan_merge[n][1],simpan_merge[n][2], done[simpan_merge[n][1] + ' ' + simpan_merge[n][2]]])
            
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow(['id_user','word1','word2','totals'])

#Untuk mengeset followers dari tiap usertarget
def createAndSetTabel3(namafile,username,jml_followers,daftarnya):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile)
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([username,jml_followers,len(daftarnya),daftarnya])
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([username,jml_followers,'panjang daftar followers',daftarnya])

#Untuk mencari followersnya user ring yang mana yang memiliki followers terbanyak
def createAndSetTabel4(namafile,user_ring,usertarget,jumlah_followers_usertarget):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile)
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([user_ring,usertarget,jumlah_followers_usertarget])
            
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow([user_ring,usertarget,jumlah_followers_usertarget])

#Untuk mengeset nama-nama pengkomen dan dicari mereka komen berapa kali
def createAndSetTabel5(namafile,daftar_komenter):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile)
        if len(daftar_komenter) > 0:
            with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
                writer = csv.writer(csvfile)
                for length in range(len(daftar_komenter)):
                    commenter = daftar_komenter[length][0]
                    for row in range(len(dataset)):
                        commenterInDataset = dataset.loc[row, 'commenters']
                        if commenter == commenterInDataset:
                            dataset.loc[row,'total komen'] += 1
                            dataset.to_csv(namafile,index = False)
                            break
                        
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile, 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow(['commenters','total komen'])

#Untuk mencari teman yang sama dari CAST3 (CAST = Create And Set Tabel)
def createAndSetTabel6(namafile,daftar_terakhir = []):
    try: #Untuk meng-set datanya, jika terjadi error maka file belum ada dan lanjut ke exception
        dataset = pd.read_csv(namafile+'_tabel3.csv')
        with open(namafile+'_tabel6.csv', 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            if len(dataset) > 1: #Supaya isinya ga cuma 1
                for row in range(len(dataset)-1):
                    daftar = dataset.loc[row, 'daftar followersnya'] #Untuk mengecek setiap baris apakah ada yang sama seperti di 'daftar_terakhir'
                    daftar.replace('[','').replace(']','').replace(',','').replace("'",'')
                    bantu = []
                    for i in range(len(daftar_terakhir)):
                        if daftar_terakhir[i] in daftar:
                            bantu.append(daftar_terakhir[i])
                    if len(bantu) > 0:
                        writer.writerow([dataset.loc[len(dataset) - 1, 'username'],dataset.loc[row, 'username'],len(bantu),bantu])
                
    except: #Karena file belum ada lalu dibuat filenya
        with open(namafile+'_tabel6.csv', 'a', newline='') as csvfile: #Membuat file '.csv'
            writer = csv.writer(csvfile)
            writer.writerow(['user 1','user 2','total teman yang sama','daftarnya'])

def getFileSize(nameFile):
    return os.stat(nameFile).st_size

def loginInstagram(url, username, password):
    browser.get(url) #Masuk ke url.
    time.sleep(2) #Memberi kesempatan untuk loading page.
    browser.find_element_by_xpath('/html/body/span/section/main/article/div[2]/div[2]/p/a').click() #Click untuk ke halaman login.
    #3 baris ke bawah berfungsi untuk mengisi form dan login.
    print("Mengisi form login ....")
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    browser.find_element_by_xpath('/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
    time.sleep(2) #Memberi kesempatan untuk loading page.
    i = 1
    while 1:
        try:
            browser.find_element_by_xpath('/html/body/div['+str(i)+']/div/div/div[3]/button[2]').click() #Menutup pop-up yang muncul.
            break
        except:
            i += 1
            if i == 10:
                i = 0
            continue
    try:
        browser.find_element_by_xpath('/html/body/span/section/nav/div[2]/div/div/div[3]/div/div[3]/a').click() #Menuju ke halaman profile user.
    except:
        browser.find_element_by_xpath('/html/body/span/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span').click() #Menuju ke halaman profile user.

def getListFollowers(username, jml_followers = 0):
    print("Sedang mengload data daftar followers " + username + " ....")
    time.sleep(2) #Untuk menunggu page profile home selesai diload
    if jml_followers == 0:
        jml_followers = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title') #Untuk mendapatkan jumlah followers users di dalam list
        jml_followers.replace(',','')
    browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a').click() #Meng-click href untuk melihat tampilan followersnya
    time.sleep(2)
    followersList = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul')
    lengthListFollowers = len(followersList.find_elements_by_css_selector('li')) #Untuk mendapatkan panjang list followers yang sudah ditampilkan
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(lengthListFollowers)+']').click()#klik bar kosong akun pertama
    daftar = []
    nilai_berulang = 0
    batas_berulang = 0
    hitung = 0
    while lengthListFollowers < int(jml_followers) and batas_berulang < 4 and lengthListFollowers < 2000:
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li[' + str(lengthListFollowers - 2) + ']').click() #Supaya bisa ngescroll sampai batas yang ditentukan
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[4]/a')
            browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(lengthListFollowers)+']').click()
            batas_berulang += 1
            continue
        except:
            pass
        
        if nilai_berulang == lengthListFollowers:
            batas_berulang += 1
        else:
            batas_berulang = 0
            
        nilai_berulang = lengthListFollowers
        ##lengthListFollowers = len(browser.find_elements_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li'))
        lengthListFollowers = len(followersList.find_elements_by_css_selector('li'))

    for i in range(1, lengthListFollowers+1):
        if int(jml_followers) > 12:
            daftar.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(i)+']/div/div[1]/div[2]/div[1]/a').get_attribute('title'))
        else:
            daftar.append(browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/ul/div/li['+str(i)+']/div/div[2]/div[1]/div/div/a').get_attribute('title'))
    return daftar

##def setListFollowers(username, listFollowers, namafile):
##    with open(namafile, 'a', newline = '') as csvfile: #Menambahkan data ke file '.csv'
##        writer = csv.writer(csvfile)
##        writer.writerow([username, '', '', '', '', listFollowers])
##    print("Sukses menginput daftar Followers " + username + " ke dalam tabel.")
##    print()
##    #Note for me:
##    #Saat pengolahan tabel nanti untuk mencari daftar followersnya dari seseorang adalah
##    #1.)Cari username dari kolom username yang daftarnya mau diambil
##    #2.)Cari yang panjang kolom daftar followersnya > 0
##    #Catatan untuk nomor 2, karena jika panjangnya == 0, kolom tersebut kosong

def writeToCSVandGTF(username, namafile): #GTF = Get Total Followers from target, GTF berguna untuk penentuan target selanjutnya.
    print('Sedang Crawling target ' + username + ' ....')
    try:
        browser.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[1]/div/h2') #Ngecek private atau ngga, kalau ngga private lanjut ke except
        return 0, 0
            
    except:
        time.sleep(2)
        translator = str.maketrans('', '', string.punctuation) #Untuk ngebuat teksnya rapih
            
        def give_emoji_free_text(text): #Untuk membuang semua emoji
            allchars = [str for str in text.encode('ascii', 'ignore').decode('utf-8')]
            emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
            clean_text = ' '.join([str for str in text.encode('ascii', 'ignore').decode('utf-8').split() if not any(i in str for i in emoji_list)])
            return clean_text

        def hashtag(text): #Untuk mendapatkan tag
            char = text.encode('ascii', 'ignore').decode('utf-8').replace('\n',' ')
            tag = []
            teks = ''
            tulis = 0
            for i in range(len(char)):
                if tulis == 1:
                    teks = teks + char[i]
                if char[i] == '#':
                    tulis = 1
                elif (char[i] == ' ' or i == len(char)-1) and teks != '':
                    teks = '#' + teks
                    tag.append(teks)
                    tulis = 0
                    teks = ''
            return tag
        
        jml_followers = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title') #Untuk mendapatkan total followers target
        jml_posts = browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[1]/span/span').text #Untuk mendapatkan total posts target
        jml_followers = jml_followers.replace(',','')
        jml_posts = jml_posts.replace(',','')
        daftar = getListFollowers(username, int(jml_followers))
        createAndSetTabel3(namafile+'_tabel3.csv', username, int(jml_followers),daftar)
        createAndSetTabel6(namafile,daftar)
        browser.get('https://www.instagram.com/'+username)
        time.sleep(2)
        
        if int(jml_posts) == 0:
            return int(jml_followers), int(jml_posts)
        
        tes = 0
        galat = 0
        benar = 1
        while benar == 1 and int(jml_posts) != 0:
            try:
                browser.find_element_by_xpath('/html/body/span/section/main/div/div['+str(tes)+']/article/div[1]/div/div[1]/div[1]').click()
                benar = 0
            except:
                tes += 1
                galat += 1
                if galat == 10:
                    break
                continue
                
        time.sleep(2)

        #Crawling post
        limit = 0
        caption = []
        while limit < int(jml_posts)-1 and int(jml_posts) != 0 and galat != 11:
            #print("Sedang crawling data posts target " + username + " ....")
            loading = False
            kanan = False
            kiri = False
            try:
                time.sleep(2)
                browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div')
                if limit > 0:
                    browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()
                    loading = True
                    kanan = True
                else:
                    browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()
                    loading = True
                    kiri = True
                    
            except:
                try:
                    ### Ini jika ada bulet-buletan loading
                    if loading:
                        if kiri:
                            time.sleep(2)
                            browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()
                            loading = False
                            kiri = False
                            continue
                        elif kanan:
                            time.sleep(2)
                            browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()
                            loading = False
                            kanan = False
                            continue                        
                    ### Sampai sini lalu hasilnya akan dikontinue ke awal, untuk ngambil pos yang sebelumnya muter-muter
                        
                    teks = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span').text #Mengambil captionnya dan menyimpannya dalam variabel teks
                    tag = hashtag(teks) #Meyimpan kumpulan tag
                    if len(tag) == 0:
                        tag = ''
                    teks = give_emoji_free_text(teks) #Menyingkirkan emoji dari teks
                    teks = teks.translate(translator).lower() #Membuat huruf menjadi kecil
                except:
                    teks = ''
                    tag = ''
                    
                try:
                    try:
                        likes = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/button/span').text #Untuk mengambil like yang punya banyak likes.
                    except:
                        likes = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/div/button').text #Untuk likes-nya sedikit
                        likes = likes.replace('like this','').replace('like','')#Untuk me-replace 'like this' atau 'like'
                except:
                    likes = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[2]/div/span/span').text #Untuk mendapatkan likes dari video

                try:
                    commentlist = len(browser.find_elements_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/ul')) #panjang dari banyak komen
                    comment = []
                    for i in range(1,commentlist+1):
                        morecomment = []
                        commentter = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/ul['+str(i)+']/div/li/div/div[1]/div[2]/h3/a').text
                        teksc = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/ul['+str(i)+']/div/li/div/div[1]/div[2]/span').text
                        teksc = give_emoji_free_text(teksc)
                        teksc = teksc.translate(translator).lower()
                        morecomment.append(commentter)
                        morecomment.append(teksc)
                        comment.append(morecomment)
                    if len(comment) == 0:
                        comment = ''
                except:
                    comment = ''
                if len(teks) > 0:
                    caption.append(teks)    
                createAndSetTabel5(namafile+'_tabel5.csv',comment)    
                createAndSetTabel1(namafile+'_tabel1.csv',username, teks, tag, likes, comment)    
                if limit == 0:
                    browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a').click()
                else:
                    try:
                        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]').click()
                    except:
                        pass
                    
                time.sleep(2)
                limit += 1
        if len(caption) != 0:
            createAndSetTabel2(namafile+'_tabel2.csv', username, caption)
        print("Sukses!")
    return int(jml_followers), int(jml_posts)


def mulaiProgram(url, username, password, namafile):
    loginInstagram(url, username, password)
    hitung = 0
    username = username
    tertinggi = 0
    sizeOfFile = 0
    daftar_k = [username]
    if username != 'rezas_esa':
        daftar_k.append('rezas_esa') #Daftar kunjungan = berisi para user yang telah dikunjungi, diisi username agar data dari user pengguna tidak juga ikut diambil
    row = 0 #Sebagai penentu row tabel3
    
    while sizeOfFile < 1024*1024*100 and hitung < 4:
        try:
            listFollowers = []
            listFollowers = getListFollowers(username, tertinggi)
            bantu = 0
            for usertarget in listFollowers:
                if usertarget not in daftar_k : #Untuk mengecek apakah usertarget pernah dikunjungi sebelumnya dan diambil beberapa item tertentu
                    browser.get(url+'/'+usertarget)
                    time.sleep(2)
                    totalFollowers, post = writeToCSVandGTF(usertarget, namafile)
                    daftar_k.append(usertarget)
                    createAndSetTabel4(namafile+'_tabel4.csv', username, usertarget, totalFollowers)
                    username = usertarget
                    bantu += 1
                    print()
                        if post < 10:
                           time.sleep(10) #Untuk menghindari terjadinya error karena terlalu banyak request
                else:
                    continue
                if bantu > 4:
            tabel3 = pd.read_csv(namafile+'_tabel3.csv')
            while 1: #Akan menelusuri tabel yang ada daftar followersnya dan diambil daftar followersnya (berurutan secara bfs)
                follower = tabel3.loc[row, 'daftar followersnya']
                follower = follower.replace('[','').replace(']','').replace(',','').replace("'",'')
                username = tabel3.loc[row, 'username']
                split = follower.split()
                for usertarget in split:
                    if usertarget not in daftar_k:
                        try:
                            browser.get(url+'/'+usertarget)
                            time.sleep(2)
                            totalFollowers, post = writeToCSVandGTF(usertarget, namafile)
                            daftar_k.append(usertarget)
                            createAndSetTabel4(namafile+'_tabel4.csv',username,usertarget,totalFollowers)
                            username = usertarget
                            print()
                            if post < 10:
                                time.sleep(10)
                        except:
                            continue
                row += 1
            
        except:
            hitung += 1
            continue
        sizeOfFile = getFileSize(namafile+'_tabel1.csv')
        
"""
  JIKA PASSWORD DI-INPUT MAKA YANG KELUAR ADALAH SIMBOL
  ASTERIK, BUKAN HURUF PASSWORD-NYA.

  DAN PROGRAM INI DAPAT DIJALANKAN DI DALAM CMD.
"""

user = input('Masukkan username akun anda: ')
passwo = prompt('Masukkan password akun anda: ', is_password = True)
namafile = input("Masukkan nama file: ")

createAndSetTabel1(namafile+'_tabel1.csv','username','caption','tag','likes','comment')
createAndSetTabel2(namafile+'_tabel2.csv','id_user','caption')
createAndSetTabel6(namafile)
createAndSetTabel3(namafile+'_tabel3.csv','username','jumlah followers','daftar followersnya')
createAndSetTabel4(namafile+'_tabel4.csv','user sebelumnya','usertarget','jumlah followers usertarget')
createAndSetTabel5(namafile+'_tabel5.csv',[])
    

url = 'https://www.instagram.com'
username = user
password = passwo
browser = webdriver.Chrome()
actionChain = webdriver.ActionChains(browser) #Mengambil ActionChains

mulaiProgram(url, username, password, namafile)
setMongo(namafile)
predictionWord(namafile)
