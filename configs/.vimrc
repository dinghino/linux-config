" ========================================================== General Config ===
" General vim configuration configuration

set nocompatible                        " Required first, changes everything
set hidden                              " Allow switch buffers w/o saving
set backspace=indent,eol,start          " Allow backspace in insert mode
set history=1000                        " :cmdline history
set showcmd                             " Commands at the bottom
set gcr=a:blinkon0                      " Disable blinking cursor
set autoread                            " Reload files changed from outside
set number                              " Display row number
set showmatch                           " Highlight matching parenthesis
set timeoutlen=250                      " Timeout for key combinations
set syntax=on                           " Enable syntax higlight

if has('mouse')                         " enable mouse if available
    set mouse=a
endif

let mapleader = ","                     " Change <Leader>

" Bashlike filename completion
set wildmenu
set wildmode=list:longest
set wildignore=*.o,*.fasl


" =============================================== Whitespaces & Indentation ===
"

set tabstop=4                           " Default tabbing spacing
set expandtab                           " Tabs become spaces
set autoindent
set smarttab
set nowrap
set scrolloff=5                         " Keep 5 lines below and above cursor

" Symbols for whitespaces
set listchars=eol:¬,tab:>·,trail:·,extends:>,precedes:<
set list                                " Display whitespaces by default


" ============================================================ Code Folding ===
"

set foldmethod=syntax
set foldnestmax=10
set nofoldenable                        " Open all folds on file open
set foldlevel=2


" ===================================================== Backup & Swap Files ===
"

set noswapfile
set nobackup
set nowb

" ========================================================= Persistent Undo ===
" Keep undo history across sessions by storing in file.

if has('persistent_undo')
  silent !mkdir ~/.vim/backups > /dev/null 2>&1
  set undodir=~/.vim/backups
  set undofile
endif

" ================================================================= Plugins ===
"

filetype off
call plug#begin('~/.vim/bundle')

" General plugins
Plug 'vim-airline/vim-airline'              " Vim Airline powerline
Plug 'vim-airline/vim-airline-themes'       " Themes for vim airline
Plug 'scrooloose/nerdtree'                  " tree view
Plug 'Xuyuanp/nerdtree-git-plugin'          " Git extension for NERDTree
Plug 'motemen/git-vim'                      " Git integration
Plug 'MikeCoder/markdown-preview.vim'       " Markdown preview

Plug 'Valloric/YouCompleteMe', {'do': 'python3.6 -m ./install.py --clang-completer --tern-completer'}

" ========== Themeing & Apperances
" Most themes use background=[dark|light] to switch mode
Plug 'kristijanhusak/vim-hybrid-material'   " hybrid_material, hybrid_reverse
Plug 'altercation/vim-colors-solarized'     " solarized
Plug 'tmux-plugins/vim-tmux'                " Tmux syntax
Plug 'ryanoasis/vim-devicons'               " Iconize stuff

" Javascript
Plug 'pangloss/vim-javascript'
Plug 'mxw/vim-jsx'

call plug#end()
filetype plugin indent on


" ================================================================= Theming ===
" Use theme plugins and other styling settings

set t_Co=256                            " 256 color mode
set background=dark
silent! colorscheme hybrid_reverse      " Set colorscheme. Fails silently
let g:enable_bold_font=1                " Bold fonts enabled
set cursorline                          " Highlight cursor line
set title                               " Override the terminal title
set ruler
set visualbell                          " Flash instead of beeping

" If running gvim also do some other stuff
if has('gui_running')
  set encoding=utf-8
  set guifont=Fira\ Mono\ for\ Powerline\ 14
  " Turn off toolbar and menu
  set guioptions-=T
  set guioptions-=m
end


" =========================================================== YouCompleteMe ===

let g:ycm_server_python_interpeter = '/usr/bin/python3.6'


" ============================================================= Vim Airline ===
"

set laststatus=2                        " Enable two rows for the statusbar
let g:airline#extensions#tabline#enabled=1
let g:airline#extensions#whitespace#enabled=1" whitespace check on save
let g:airline_powerline_fonts=1
let g:airline_theme='base16'


" ================================================================ NERDTree ===
"

let NERDTreeAutoDeleteBuffer=1
let NERDTreeMinimalUI=0
let NERDTreeDirArrows=1

" Open nerdtree at vim startup only if no file has been specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" Close VIm if NERDTree is the only window left
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
" NERDTress File highlighting

function! NERDTreeHighlightFile(extension, fg, bg, guifg, guibg)
exec 'autocmd filetype nerdtree highlight ' . a:extension .' ctermbg='. a:bg .' ctermfg='. a:fg .' guibg='. a:guibg .' guifg='. a:guifg
exec 'autocmd filetype nerdtree syn match ' . a:extension .' #^\s\+.*'. a:extension .'$#'
endfunction

call NERDTreeHighlightFile('jade', 'green', 'none', 'green', '#151515')
call NERDTreeHighlightFile('ini', 'yellow', 'none', 'yellow', '#151515')
call NERDTreeHighlightFile('md', 'blue', 'none', '#3366FF', '#151515')
call NERDTreeHighlightFile('yml', 'yellow', 'none', 'yellow', '#151515')
call NERDTreeHighlightFile('config', 'yellow', 'none', 'yellow', '#151515')
call NERDTreeHighlightFile('conf', 'yellow', 'none', 'yellow','#151515')
call NERDTreeHighlightFile('json', 'yellow', 'none', 'yellow','#151515')
call NERDTreeHighlightFile('html', 'yellow', 'none', 'yellow', '#151515')
call NERDTreeHighlightFile('styl', 'cyan', 'none', 'cyan', '#151515')
call NERDTreeHighlightFile('css', 'cyan', 'none', 'cyan', '#151515')
call NERDTreeHighlightFile('coffee', 'Red', 'none', 'red', '#151515')
call NERDTreeHighlightFile('js', 'Red', 'none', '#ffa500', '#151515')
call NERDTreeHighlightFile('php', 'Magenta', 'none', '#ff00ff', '#151515')


" ============================================================ Vim DevIcons ===

let g:webdevicons_enable=1
let g:webdevicons_enable_nerdtree=1
let g:webdevicons_enable_airline_tabline=1
let g:webdevicon_enable_ariline_statusline=1


" ============================================================= Key mapping ===

map <C-n> :NERDTreeToggle<CR>             " Map ctrl-n to nerdtree
map <silent> <leader>s :set nolist!<CR>   " Toggle whitespaces display
nmap <silent> <C-n> :silent :nohlsearch<CR> " Toggle highlighting


" =============================================================== Behaviour ===
" Various behavioural mapping

" Toggle is mapped on Mapping section
" Scroll faster
nnoremap <C-e> 3<C-e>
nnoremap <C-y> 3<C-y>
vnoremap <C-e> 3<C-e>
vnoremap <C-y> 3<C-y>

" Auto indent pasted text
nnoremap p p=`]<C-o>
nnoremap P P=`]<C-o>


" ============================================== Language specific settings ===
"
autocmd FileType javascript,html set ts=2 shiftwidth=2 expandtab
autocmd Filetype python set ts=4 shiftwidth=2 expandtab


" =============================================================== Functions ===
"
"

" Inndent XML readably
function! DoPrettyXML()
        1,$!xmllint --format --recover -
        set filetype=xml
endfunction
command! PrettyXML call DoPrettyXML()
