" Set color scheme
colorscheme pablo
" Set tab behaviors
set tabstop=8 softtabstop=0 expandtab shiftwidth=2 smarttab
"highlight trailing whitespace in red
highlight ExtraWhitespace ctermbg=RED
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/
"Remove trailing whitespace on save
autocmd BufWritePre * :%s/\s\+$//e
"Show line numbers
"set number
"Turn on/off line numbers with ctrl-n hotkey
function! NumberToggle()
  if(&number == 1) "|| &relativenumber == 1)
    set nonumber
"    set norelativenumber
  else
    set number
  endif
endfunc
nnoremap <C-n> :call NumberToggle()<cr>
"Turn on/off relative number with ctrl-r hotkey
function! RelativeNumberToggle()
  if(&relativenumber == 1)
    set norelativenumber
  else
    set relativenumber
  endif
endfunc
nnoremap <C-r> :call RelativeNumberToggle()<cr>
"Disable automatic comment insertion
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

