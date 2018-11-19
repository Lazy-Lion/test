## 工作区、暂存区
  版本库中最重要的就是暂存区(stage or index)；创建版本库时,git 自动创建了唯一一个分支 master，git add 实际把文件修改加到暂存区中，git commit往master分区上提交修改。
  
## Fast Forward
 [merge](https://backlog.com/git-tutorial/cn/stepup/stepup1_4.html)

## .gitignore 文件
 让版本控制系统忽略某些文件

## .gitkeep 文件
 Git does not track empty directories, if you wish to track or push an empty directory to your upstream, just create one .gitkeep file. It is important to check that you never add ".gitkeep" into the .gitignore. Then the whole purpose of the tracking the empty directories would vanish.

## [github设置添加ssh](https://www.cnblogs.com/chuyanfenfei/p/8035067.html)

## 简单命令

| Command | Purpose | Info |
| - | - | - |
| git config \-\-global user.name "name" | 配置用户名 | 安装完git后需要先配置 |
| git config \-\-global user.email "email" | 配置邮箱 | 安装完git后需要先配置 |
| git config \-\-global alias.co checkout | 配置checkout别名为co | | 
| git init | 创建git版本仓库 | 生成.git文件夹 |
| git status | 查看git仓库状态 | | 
| git log | 日志记录 | |
| git reflog | 可以获取git commands 和 commit id | |
| git add filename | 添加文件 | |
| git commit -m "message" | 提交文件 | 可以提交之前add 的多个文件,message为提交说明 |
| git reset \-\-hard HEAD^ | 退回到前一个版本 | |
| git reset \-\-hard commit_id | 退回到指定commit id 对应的版本 | |
| git diff HEAD \-\- filename | 查看工作区和版本库最新版本的区别 | 注意 \-\- 和filename直接有空格|
| git rm filename | 删除文件 | 执行过后需要commit | 
| git checkout -- filename | 丢弃未到暂存区的工作区的修改 | 撤回到最近一次git add 或 git commit 时的状态; 对于手动误删或使用rm误删但未提交的文件，可以使用该命令恢复，但是使用git rm命令删除的即使没有commit 也不能恢复|
| git reset HEAD filename | 将暂存区的修改退回到工作区 | 可以与上条命令配合使用，撤销已提交到暂存区的修改 |
| git remote add origin git@servername:path/reponame.git | 关联远程仓库,如 git remote add origin git@github.com:Lazy-Lion/test.git | 关联github时需要ssh才能推送| 
| git remote remove origin | 取消本地目录下关联的远程库 | |
| git push -u origin master | 第一次推送master分支上所有内容到远程仓库 | |
| git push origin branchname | 后续从本地推送修改到远程仓库 | 如果推送失败，先用git pull抓取远程新的提交,若有冲突处理冲突 |
| git fetch origin | 从远程获取最新版本到本地，不会自动合并，如 git fetch origin master | |
| git pull | 从远程获取最新版本到本地，自动合并| git pull origin master 相当于 git fetch origin master + git merge origin/master |
| git checkout -b branchname origin/branchname | 在本地创建和远程分支对应的分支 | 本地和远程分支名最好一致 |
| git branch --set-upstream branchname origin/branchname | 建立本地分支和远程分支的关联 | | 
| git clone git@github.com:Lazy-Lion/test.git | 远程仓库克隆到本地 | 该命令为克隆我的test仓库；git 支持多种协议(ssh,https等)，通过ssh支持的原生git协议最快 |
| git remote -v | 查看远程库信息 | |  
| git checkout -b dev | 创建dev分支，并切换到该分支| 相当于 git branch dev ; git checkout dev |
| git branch | 查看分支 | | 
| git merge dev | 合并分支 | 切换到master分支，执行该命令，合并dev 到 master；使用git merge 合并分支时如果遇到冲突，合并的文件会整合2个分支的内容，根据提示**手动**修改之后再add -> commit ，完成合并 |
| git merge --no-ff -m "message" dev | 使用普通模式合并 | 合并分支默认采用Fast Forward 模式 |
| git branch -d dev | 删除dev 分支 | |
| git branch -D dev | 删除没有被合并过的分支dev | |
| git stash | 当前分支手头工作尚未提交，可以使用该指令保存工作现场，转而创建新的分支，完成之后使用git stash pop 回到工作现场 | |
| git stash list | 显示stash 列表 | |
| git rebase | | 合并多个commit 为一个完整的commit |
| git tag tagname | 创建标签 | 也可以指定一个commit id, git tag tagname commitid |
| git tag -a tagname -m "message" | 创建标签并添加标签信息 | |
| git tag | 展示标签列表 | |
| git show tagname | 查询标签信息 | git 的标签与 commit 关联，若不同分支有同一个commit，则多个分支同时存在该标签|
| git push origin tagname | 推送一个本地标签 | |
| git push origin tags | 推送全部未推送过的标签 | | 
| git tag -d tagname | 删除一个本地标签 | |
| git push origin :ref/tags/tagname | 删除一个远程标签 | |







 
