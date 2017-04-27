" Vundle config
    set nocompatible                                " required by vundle
    filetype off                                    " required by vundle
    " Runtime path for vundle
    call plug#begin('~/.vim/bundle')

      Plug 'vim-airline/vim-airline'              " Vim Airline powerline
      Plug 'vim-airline/vim-airline-themes'       " Themes for vim airline
      Plug 'kristijanhusak/vim-hybrid-material'   " colorschemes
      Plug 'scrooloose/nerdtree'                  " tree view
      Plug 'ryanoasis/vim-devicons'               " Iconize stuff
      Plug 'motemen/git-vim'                      " Git integration
      Plug 'MikeCoder/markdown-preview.vim'       " Markdown preview
      " Autocompletion
      Plug 'Valloric/YouCompleteMe', { 'do': './install.sh --clang-completer --tern-completer' }

    call plug#end()
    filetype plugin indent on

" Make YouCompleteMe work with python3.6
    let g:ycm_server_python_interpeter = '/usr/bin/python3.6'

" Basic configuration and theming
    set hidden                                      " ctrlspace
    set number                                      " row numbers
    silent! colorscheme hybrid_reverse              " if not found will say nothing
    let g:enable_bold_font=1
    set background=dark

    if has('mouse')                                 " enable mouse if available
        set mouse=a
    endif

    set cursorline                                  " highlight current line
    set wildmenu                                    " command tab menu
    set showmatch                                   " show matching parenthesis
    set timeoutlen=250                              " timeout for ESC commands

" whitespace and tabs configuration
    set tabstop=4
    set autoindent
    set expandtab                                   " tabs become spaces
    " symbol definition for whitespaces
    set listchars=eol:¬,tab:>·,trail:·,extends:>,precedes:<
    set list

" code folding config
    set foldmethod=syntax
    set foldnestmax=10
    set nofoldenable                                " open all folds on file open
    set foldlevel=2


" vim-airline config
    set t_Co=256
    set laststatus=2
    let g:airline#extensions#tabline#enabled=1
    let g:airline#extensions#whitespace#enabled=1   " whitespace check on save
    let g:airline_powerline_fonts=1
    let g:airline_theme='base16'

" NERDTree config
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

" Font setup
    set guifont=Fira\ Mono\ for\ Powerline\ 14     " does not work!

" Vim-DevIcons setup
    let g:webdevicons_enable=1
    let g:webdevicons_enable_nerdtree=1
    let g:webdevicons_enable_airline_tabline=1
    let g:webdevicon_enable_ariline_statusline=1

" Back and swap files
    set backup
    set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
    set backupskip=/tmp/*,/private/tmp/*
    set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
    set writebackup
