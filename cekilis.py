from InstagramAPI import InstagramAPI
import time
import json

def getTotalFollowings(api, user_id):
    following = []
    next_max_id = True
    while next_max_id:
        #print(next_max_id)
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''
        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following


def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from PyInstagramAPI
    """
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def findAdded(old, new):
    result = []
    for a in new:
        found = False
        for b in old:
            if a['pk'] == b['pk']:
                found = True
        if not found:
            result.append(a)
    return result

def save(data, name):
    with open(name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def writeNames(followers):
    follower_list = []
    for a in followers:
        follower_list.append(a['username'])
    print(follower_list)


def findLikedPosts(user_id, last_id = '', repeat_num = 0):
    api.getUserFeed(user_id, last_id)
    data = api.LastJson
    save(data, 'control.json')
    result = []
    iter_result = -1
    i = 0
    for a in data['items']:
        if a['has_liked'] == True:
            result.append(a)
            iter_result = i
            break
        i = i+1
    if result == []:
        if data['more_available'] and repeat_num < 3:
            return findLikedPosts(user_id, data["next_max_id"], repeat_num+1)
    return result, iter_result

def findNeededPages(text):
    text = text + ' '
    started = False
    pages = []
    word = ''
    text = text.replace('\n', ' ')
    for a in text:
        if a == '@':
            started = True
        if started :
            if a != ' ' and  a != ')' and  a != '}' and  a != ']':
                word = word + a
            else:
                pages.append(word)
                word = ''
                started = False
    return pages

def isMoreOperationNeeded(pages):
    for i in range(len(pages)):
        for j in range(i+1, len(pages)):
            if(pages[i]== pages[j]):
                return True
    return False

def followWithNames(api, names):
    ids = namesToUsers(api,names)
    #save(ids, 'control.json')
    followWithUsers(api, ids)


#bu isimde bir user olmayabilir
def namesToUsers(api, names):
    users = []
    for a in names:
        succesful = api.searchUsername(a)
        if succesful:
            users.append(api.LastJson)
    return users


def followWithUsers(api, ids):
    for a in ids:
        api.follow(a['user']['pk'])

def howManyCommentsNeeded(comments):
    numList = []
    for a in comments['comments']:
        text = a['text']
        numList.append(howManyAt(text))
    return findMode(numList)


def howManyAt(text):
    num = 0
    for a in text:
        if a == '@':
            num = num+1
    return num

def findMode(liste):
    diction = {}
    for a in liste:
        if not diction.keys().__contains__(a):
            diction[a] = 1
        else:
            diction[a] = diction[a]+1
    values = list(diction.items())
    max_num = values[0][1]
    iter = values[0][0]
    for a in values:
        if a[1] > max_num:
            max_num = a
            iter = a[0]
    return iter

def createCommentText(labels, doublelabels, triplelabels, num_of_labels):
    if num_of_labels == 2:
        return doublelabels
    if num_of_labels == 3:
        return triplelabels
    if num_of_labels == 0:
        return []
    comment_list = []
    i=0
    while i < len(labels)-num_of_labels+1:
        comment = ''
        for j in range(num_of_labels):
            comment = comment + labels[i] + ' '
            i = i + 1
        comment_list.append(comment)
    return comment_list

def getLabelLists(name):
    f = open(name)
    line = ' '
    result = []
    while True:
        line = f.readline()
        if line == '':
            break
        result.append(line[0:-1])
    return result

def whetherLikeOtherPosts(text):
    key_words = ['bundan onceki', 'bundan önceki', 'daha onceki', 'daha önceki', 'gonderiden onceki', 'gönderiden önceki', 'son']
    key_words2 = ['gonderiyi', 'gönderiyi', 'gonderileri', 'gönderileri', 'postu', 'postlari', 'postları']
    found1 = False
    found2 = False
    for a in key_words:
        if a in text:
            found1 = True
    for a in key_words2:
        if a in text:
            found2 = True
    return found1 and found2

def changeAccount(name):
    label_list = getLabelLists('isimler_' + name + '.txt')
    triple_label_list = getLabelLists('uclu_isimler_' + name + '.txt')
    double_label_list = getLabelLists('ikili_isimler_' + name + '.txt')

    f = open('hesap_' + name + '.txt')
    username = f.readline()
    password = f.readline()

    api = InstagramAPI(username, password)
    api.login()

    return api, label_list, double_label_list, triple_label_list

def likeOtherPosts(api):
    pass



if __name__ == "__main__":
    name = "kullanici"

    print('hesap hazirlaniyor...')
    api, label_list, double_label_list, triple_label_list = changeAccount(name)
    user_id = api.username_id
    user = name

    while True:
        print()
        print('ornek komutlar: basla, bitir, posts, katil')
        print(user +'> komutunuz:')
        inp = input()
        if inp == 'basla':
            followings = getTotalFollowings(api, user_id)
            print(str(len(followings)) + ' kisi takip ediyorsun')
            save(followings, 'lastMyFollowings.json')
            print('lastMyFollowers.json guncellendi')
        elif inp == 'bitir':
            f = open("lastMyFollowings.json")
            old_followings = json.load(f)
            print(str(len(old_followings)) + ' kisi takip ediyordun')
            followings = getTotalFollowings(api, user_id)
            print('su anda '+ str(len(followings)) + ' kisi takip ediyorsun')
            difference = findAdded(old_followings, followings)
            print("farkli takipcilerin:")
            writeNames(difference)
            save(difference, 'difference.json')
            print('difference.json guncellendi')
        elif inp == 'merhaba':
            print('merhaba')
        elif inp == 'kapat':
            print('bye')
            break
        elif inp == 'posts':
            f = open("difference.json")
            difference = json.load(f)
            all_posts = []
            print('postlar araniyor...')
            for a in difference:
                id = a['pk']
                media, iter_result = findLikedPosts(id)
                all_posts.extend(media)
                if media == []:
                    print(a['username'] +"'in postu bulunamadi (sayfayi takip edip hicbir gonderisini begenmedin mi ki?)")
                else:
                    print(a['username'] +"'in " + str(iter_result+1) + "'inci postu")
            print('tum medyalar bulundu')
            save(all_posts, 'posts.json')
            print('posts.json guncellendi')

        elif inp == 'katil':
            f = open("posts.json")
            posts = json.load(f)
            # posts[0]['caption']['text']
            for a in posts:
                print('-------------------------------------------------------')
                print(a['user']['username'] + " 'in postu")
                print('aciklama: ' + a['caption']['text'])
                print()
                pages = findNeededPages(a['caption']['text'])
                for i in range(len(pages)):
                    pages[i] = pages[i][1:]
                print('bu sayfalar takip ediliyor... > '+ str(pages))
                api.follow(a['user']['pk'])
                api.like(a['id'])
                followWithNames(api,pages)
                api.getMediaComments(str(a['pk']), '')
                media_comments = api.LastJson
                save(media_comments, 'media_comments.json')
                if 'comments' not in media_comments.keys():
                    print('Yorumlar kapali. Kimse etiketlenmiyor')
                    print('!Programin yeterli olmadigi tespit edildi!')
                else:
                    num_of_labels = howManyCommentsNeeded(media_comments)
                    print('bir yorumda '+ str(num_of_labels) + ' tane kisi etiketleniyor')
                    comments_list = createCommentText(label_list, double_label_list, triple_label_list, num_of_labels)
                    for b in comments_list:
                        succesful = api.comment(a['id'], b)
                        if succesful:
                            print('yazilan comment > ' + b)
                        else:
                            print('gonderilemiyen comment > ' + b)
                        time.sleep(5)
                if isMoreOperationNeeded(pages):
                    print('!Programin yeterli olmadigi tespit edildi!')

                if whetherLikeOtherPosts(a['caption']['text']):
                    print('baska postlarin da begenilmesi gerektigi saptandi!')
                    print('!Programin yeterli olmadigi tespit edildi!')
                print('-------------------------------------------------------')

        elif inp == 'emoji':
            print('kac tane etiketlensin: ')
            num_of_emojies = int(input())
            f = open("posts.json")
            posts = json.load(f)
            # posts[0]['caption']['text']
            for a in posts:
                print('-------------------------------------------------------')
                print(a['user']['username'] + " 'in postu")
                print('aciklama: ' + a['caption']['text'])
                print()

                emoji_list = ['😃', '😄', '😁', '😆', '😅', '😂', '🤣', '🙂', '🙃', '😉', '😍', '😋', '😝', '🤚', '🖐', '✋', '👌', '🙋', '👊', '😙', '🐶', '🐱', '🐭', '🐹', '🐰',' 🐵', '🙈', '🙉', '🙊','🐔', '🦁', '🍎', '🍏']
                j = 0
                for i in range(num_of_emojies):
                    succesful = api.comment(a['id'], emoji_list[j])
                    if succesful:
                        print(str(i+1)+'. yazilan comment > ' + emoji_list[j])
                    else:
                        print('gonderilemiyen comment > ' + emoji_list[j])
                    time.sleep(5)
                    j = j + 1
                    if j==len(emoji_list):
                        j = 0
                print('tamamlandi')


        elif inp == 'takipten cik':
            f = open("difference.json")
            difference = json.load(f)
            print("farkli takipcilerin:")
            writeNames(difference)
            while True:
                print('bu sayfalari takipten cikmak istiyor musun(evet/hayir):')
                inp2 = input()
                if inp2 == 'evet':
                    for a in difference:
                        succesful = api.unfollow(a['pk'])
                        if succesful:
                            print(str(a['username']) + ' takipten cikildi')
                        else:
                            print(str(a['username']) + ' takipten cikarilma islemi basarisiz oldu')
                    print('tamamlandi')
                    break
                elif inp2 == 'hayir':
                    print('takipten cikma islemi iptal edildi')
                    break
                else:
                    print('gecersiz komut')

        elif inp == 'hesap':
            while True:
                print('secmek istediginiz hesabin ismini girin(damla/mustafa): ')
                name = input()
                print('hesap hazirlaniyor...')
                api, label_list, double_label_list, triple_label_list = changeAccount(name)
                user_id = api.username_id
                user = name
                break

        else:
            print('gecersiz komut')
