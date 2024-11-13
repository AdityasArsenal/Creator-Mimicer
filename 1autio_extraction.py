from moviepy.editor import VideoFileClip

def video_to_audio(vid_url,path):

    vid = VideoFileClip(vid_url)
    aud = vid.audio
    aud.write_audiofile(fr"{path}")

video_url_from_web = 'https://scontent.cdninstagram.com/o1/v/t16/f1/m82/6E4B82C1ECA552944D3928CCF83318AD_video_dashinit.mp4?efg=eyJ4cHZfYXNzZXRfaWQiOjk4Mjk5ODA4OTM3ODk2MywidmVuY29kZV90YWciOiJ4cHZfcHJvZ3Jlc3NpdmUuSU5TVEFHUkFNLkNMSVBTLkMzLjQ4MC5kYXNoX2Jhc2VsaW5lXzJfdjEifQ&_nc_ht=instagram.fiev22-2.fna.fbcdn.net&_nc_cat=102&vs=e1cecd1db07d261e&_nc_vs=HBksFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC82RTRCODJDMUVDQTU1Mjk0NEQzOTI4Q0NGODMzMThBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dHY2ZraFRscXNZQUxvc0RBRVE1UGtkMEJyOE9icV9FQUFBRhUCAsgBACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJqay9b6Cgr8DFQIoAkMzLBdAS9mZmZmZmhgSZGFzaF9iYXNlbGluZV8yX3YxEQB1_gcA&ccb=9-4&oh=00_AYAAiKP0N6nwCT-e24nKhiMmzg9EIa4iL-oSCpHfFZ9DkQ&oe=67362940&_nc_sid=1d576d'

given_path = r"C:\Users\24adi\OneDrive\Desktop\intern\AI system Internship\AI-System\audios\neww.mp3"

video_to_audio(video_url_from_web,given_path)