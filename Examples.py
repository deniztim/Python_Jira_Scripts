from jira import JIRA

#options = {
#    'server': 'http://localhost:8080'}
jira = JIRA('http://localhost:8080',basic_auth=('admin','123'),kerberos=True)

issues = jira.search_issues('project = 10000 AND assignee!=currentUser()',maxResults=0)


issue = jira.issue('MYP-6')
summary = issue.fields.summary
issue.fields.worklog.worklogs
issue.fields.worklog.worklogs[0].author
issue.fields.worklog.worklogs[0].timeSpent
issue.fields.worklog.worklogs[0].updated

jira.assign_issue(issue, 'Anakin')
transitions = jira.transitions(issue)
transition_serie = [(t['id'], t['name']) for t in transitions]

comments_b = jira.comments(issue)
print (comments_b)
comment = jira.comment('MYP-6', '10300')
print (comment.body)

issue_dict = {
    'project': {'id': 10000},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Snake'},
}
new_issue = jira.create_issue(fields=issue_dict)
