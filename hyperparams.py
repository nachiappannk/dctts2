# -*- coding: utf-8 -*-
class Hyperparams:
	'''Hyperparameters'''

	data_dir = 'dataset/'
	data = 'dataset/'
	metafile = 'dataset/metadata.csv'
	batch_size = 16 # alias = N
	warmup_steps = 4000
	logdir = 'logdir' # log directory
	logdirmag = 'logdirmag' # log directory
	logdirmel = 'logdirmel' # log directory
	sr = 22050
	n_fft = 2048 # fft points (samples)
	fd = 1+n_fft//2
	frame_shift = 0.0125 # seconds
	frame_length = 0.05 # seconds
	hop_length = 256 # samples	This is dependent on the frame_shift.
	win_length = 1024 # samples This is dependent on the frame_length.
	n_mels = 80 # Number of Mel banks to generate
	sharpening_factor = 1.4 # Exponent for amplifying the predicted magnitude
	n_iter = 50 # Number of inversion iterations
	preemphasis = .97 # or None
	griffin_lim_iters=60
	power=1.5              # Power to raise magnitudes to prior to Griffin-Lim

	max_db = 100
	min_db = -100
	ref_db = 20
	max_grad_norm = 100.
	max_grad_val = 5.
	
	# model
	maxlen = 180 # Maximum number of letters in a sentance = T.
	Ty = 868 # Max number of timesteps 
	Tyr = Ty//4 # Max number of timesteps 
	e = 128
	d = 256
	c = 512
	lr = 2e-4
	init_lr=2e-4
	g=0.2
	b1 = 0.5
	b2 = 0.9
	eps = 1e-6
	logevery = 200	
	dropout_rate = 0.1
	masking = False
	
	
	
