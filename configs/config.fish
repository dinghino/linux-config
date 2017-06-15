setenv SSH_ENV $HOME/.ssh/environment

function start_agent
    echo "Initializing new SSH agent ..."
    ssh-agent -c | sed 's/^echo/#echo/' > $SSH_ENV
    echo "succeeded"
            chmod 600 $SSH_ENV
    . $SSH_ENV > /dev/null
    ssh-add
end

function test_identities
    ssh-add -l | grep "The agent has no identities" > /dev/null
    if [ $status -eq 0 ]
        ssh-add
        if [ $status -eq 2 ]
            start_agent
        end
    end
end

if [ -n "$SSH_AGENT_PID" ]
    ps -ef | grep $SSH_AGENT_PID | grep ssh-agent > /dev/null
    if [ $status -eq 0 ]
        test_identities
    end
else
    if [ -f $SSH_ENV ]
        . $SSH_ENV > /dev/null
    end
    ps -ef | grep $SSH_AGENT_PID | grep -v grep | grep ssh-agent > /dev/null
    if [ $status -eq 0 ]
        test_identities
    else
        start_agent
    end
end

eval (python3.6 -m virtualfish)
source ~/.config/fish/nvm-wrapper/nvm.fish 

function ..
    cd ..
end

# git fech origin of current branch and checkout
function gcopr
    git fetch origin ull/$argv/heade:pr-$argv; and git checkout pr-$argv;
end


# git pretty log
function gpl
    clear; and git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %Cbold%s%Creset %Cgreen(%cr) %Cblue<%an>%Creset' --abbrev-commit
end
