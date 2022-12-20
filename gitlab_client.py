import gitlab

gl = gitlab.Gitlab(url='http://192.168.3.56:8098', private_token='UJFWJWcxvWciPuQDugxu')
projects = gl.projects.list(get_all=True)
commits = projects[1].commits.list(ref_name='dev')
print(commits[0])