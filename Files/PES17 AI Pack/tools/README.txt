---------------------------------- bin.py ----------------------------------
Used to process the AI binaries. Outputs the binary-specific index file and
the data files contained in that binary.

Input:
 - Header length is the length of the datablock starting from the beginning
   of the file and ending before the first file entry in the binary, in DEC.
    For example, for constant_match the length 284 bytes.
 - Index length is the length of the datablock containing the names of the 
   files packed into the binary, in DEC. This also includes all the padding
   0x00, so be careful or all the extracted data files will be off. For
   example, for constant_match the length is 356 bytes.
 - Binary file takes a value of 0-2, and was made like this simply because
   there are only 3 files to unpack and typing the filename fully gets
   annoying after a while. 0 is constant_match.bin, 1 is constant_player.bin
   and 2 is constant_team.bin
   
---------------------------------- fill.py ---------------------------------
More of a quality of life tool, used to populate the "reconst" folder with
empty files with correct filenames quickly. You won't need this unless you're
trying to build a new set of reconstructed files.

Input:
  - Doesn't take any. Put in the folder with the extraced data files and an
    empty "reconst" folder and it'll do its job.