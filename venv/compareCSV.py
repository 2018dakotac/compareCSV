import pandas as pd
import datetime


# compares contents of csv simulation file outputs. Written by Dakota C. March 2020

def comparefile(folder, simulation, threads):
    # make timestamped log file
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H.%M")
    log = timestamp + '_log.txt'
    log_file = open(log, 'a')
    # time stamped error file
    error_report = timestamp + '_error_report.txt'
    error_file = open(error_report, 'a')
    # TODO: make better timestamp system

    # open file to test
    path = '/mnt/d/SIMTX2/'
    filename = path + folder + '/' + threads + 'T/' + simulation + '.csv'
    print('Accessing', filename)
    log_file.write('Accessing {}\n'.format(filename))
    f2 = pd.read_csv(filename.capitalize())

    # opening original file
    originalfilename = 'baseline/' + threads + 'T/' + simulation + '.csv'
    f1 = pd.read_csv(originalfilename)

    # checks the two files
    log_file.write(simulation)
    ncol = len(f1.columns)
    i = 0
    print(f1.iloc[0, i])
    log_file.write('{}\n'.format(f1.iloc[0, i]))
    while i < ncol:
        print('Column:', i)
        log_file.write("Column: {}\n".format(i))
        print('standard:', f1.iloc[0, i], ' current:', f2.iloc[0, i])
        log_file.write('standard: {} current: {}\n'.format(f1.iloc[0, i], f2.iloc[0, i]))
        if f1.iloc[0, i] != f2.iloc[0, i]:
            print('**********************MISMATCH*************************')
            log_file.write('**********************MISMATCH*************************\n')
            # makes error report
            error_file.write('ERROR FOUND! Simulation: {} Thread Config: {}T\n'.format(simulation, threads))
            error_file.write("Column: {}\n".format(i))
            error_file.write('standard: {} current: {}\n'.format(f1.iloc[0, i], f2.iloc[0, i]))
            error_file.write('**********************MISMATCH*************************\n')
        i = i + 1
    print('Finished checking', filename)
    log_file.write('Finished checking {}\n\n'.format(filename))
    log_file.close()


folderName = input('What is the name of the folder containing output directory\n')
# theadConfig = input('What thread configuration do you want to test\n')

# TESTING 1T
comparefile(folderName, 'fluidanimate', '1')
comparefile(folderName, 'blackscholes', '1')
comparefile(folderName, 'pathfinder', '1')
# comparefile(folderName, 'swaptions', '1')
comparefile(folderName, 'backprop', '1')
comparefile(folderName, 'volrend', '1')
comparefile(folderName, 'hotspot', '1')
comparefile(folderName, 'barnes', '1')
# comparefile(folderName, 'kmeans', '1')
comparefile(folderName, 'lavamd', '1')
comparefile(folderName, 'stream', '1')
comparefile(folderName, 'radix', '1')
comparefile(folderName, 'srad', '1')
comparefile(folderName, 'bfs', '1')
comparefile(folderName, 'fft', '1')
comparefile(folderName, 'fmm', '1')
print("OMITTING 1x1T SWAPTIONS FIX THEN ADD IT BACK TO TEST")
print("OMITTING 1x1T KMEANS FIX THEN ADD IT BACK TO TEST")

# TESTING 4x1T
comparefile(folderName, 'fluidanimate', '4x1')
comparefile(folderName, 'blackscholes', '4x1')
comparefile(folderName, 'pathfinder', '4x1')
comparefile(folderName, 'swaptions', '4x1')
comparefile(folderName, 'backprop', '4x1')
comparefile(folderName, 'volrend', '4x1')
comparefile(folderName, 'hotspot', '4x1')
comparefile(folderName, 'barnes', '4x1')
comparefile(folderName, 'kmeans', '4x1')
comparefile(folderName, 'lavamd', '4x1')
comparefile(folderName, 'stream', '4x1')
comparefile(folderName, 'radix', '4x1')
comparefile(folderName, 'srad', '4x1')
comparefile(folderName, 'bfs', '4x1')
comparefile(folderName, 'fft', '4x1')
comparefile(folderName, 'fmm', '4x1')

# TESTING 4x2
comparefile(folderName, 'fluidanimate', '4x2')
comparefile(folderName, 'blackscholes', '4x2')
comparefile(folderName, 'pathfinder', '4x2')
comparefile(folderName, 'swaptions', '4x2')
comparefile(folderName, 'backprop', '4x2')
comparefile(folderName, 'volrend', '4x2')
comparefile(folderName, 'hotspot', '4x2')
comparefile(folderName, 'barnes', '4x2')
comparefile(folderName, 'kmeans', '4x2')
comparefile(folderName, 'lavamd', '4x2')
comparefile(folderName, 'stream', '4x2')
comparefile(folderName, 'radix', '4x2')
comparefile(folderName, 'srad', '4x2')
comparefile(folderName, 'bfs', '4x2')
comparefile(folderName, 'fft', '4x2')
comparefile(folderName, 'fmm', '4x2')

# TESTING 4x4
comparefile(folderName, 'fluidanimate', '4x4')
# comparefile(folderName, 'blackscholes', '4x4')
comparefile(folderName, 'pathfinder', '4x4')
# comparefile(folderName, 'swaptions', '4x4')
comparefile(folderName, 'backprop', '4x4')
comparefile(folderName, 'volrend', '4x4')
comparefile(folderName, 'hotspot', '4x4')
comparefile(folderName, 'barnes', '4x4')
comparefile(folderName, 'kmeans', '4x4')
comparefile(folderName, 'lavamd', '4x4')
comparefile(folderName, 'stream', '4x4')
comparefile(folderName, 'radix', '4x4')
comparefile(folderName, 'srad', '4x4')
comparefile(folderName, 'bfs', '4x4')
comparefile(folderName, 'fft', '4x4')
comparefile(folderName, 'fmm', '4x4')
print("OMITTING 4x4T SWAPTIONS FIX THEN ADD IT BACK TO TEST")
print("OMITTING 4x4T BLACKSCHOLES FIX THEN ADD IT BACK TO TEST")

# TESTING 8x4
comparefile(folderName, 'fluidanimate', '8x4')
comparefile(folderName, 'blackscholes', '8x4')
comparefile(folderName, 'pathfinder', '8x4')
comparefile(folderName, 'swaptions', '8x4')
comparefile(folderName, 'backprop', '8x4')
comparefile(folderName, 'volrend', '8x4')
comparefile(folderName, 'hotspot', '8x4')
comparefile(folderName, 'barnes', '8x4')
comparefile(folderName, 'kmeans', '8x4')
comparefile(folderName, 'lavamd', '8x4')
comparefile(folderName, 'stream', '8x4')
comparefile(folderName, 'radix', '8x4')
comparefile(folderName, 'srad', '8x4')
comparefile(folderName, 'bfs', '8x4')
comparefile(folderName, 'fft', '8x4')
comparefile(folderName, 'fmm', '8x4')

# TESTING 16T
comparefile(folderName, 'fluidanimate', '16')
comparefile(folderName, 'blackscholes', '16')
comparefile(folderName, 'pathfinder', '16')
comparefile(folderName, 'swaptions', '16')
comparefile(folderName, 'backprop', '16')
comparefile(folderName, 'volrend', '16')
comparefile(folderName, 'hotspot', '16')
comparefile(folderName, 'barnes', '16')
comparefile(folderName, 'kmeans', '16')
comparefile(folderName, 'lavamd', '16')
comparefile(folderName, 'stream', '16')
comparefile(folderName, 'radix', '16')
comparefile(folderName, 'srad', '16')
comparefile(folderName, 'bfs', '16')
comparefile(folderName, 'fft', '16')
comparefile(folderName, 'fmm', '16')
