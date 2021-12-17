var player = document.getElementById('player__source'),
		playLoading = document.querySelectorAll('.player__loading span'),
		playPause = document.getElementById('playPause'),
		currentTime = document.getElementById('currentTime'),
		seek = document.getElementById('seek'),
		durationTime = document.getElementById('durationTime'),
		muted = document.getElementById('muted'),
		timeInterval,
		i,
		len = playLoading.length;

window.onload = function() {
	playPause.addEventListener('click', playPauseMusic, false);
	muted.addEventListener('click', mutedMusic, false);
	player.addEventListener('ended', endedMusic, false);
};

// Play and Pause Music
function playPauseMusic() {
	var i, len = playLoading.length;
	if (player.paused) {
		player.play();
		timeInterval = setInterval(timeUpdateMusic, 100);
		seek.addEventListener('change', seekMusic, false);
		playPause.classList.remove('icon-play');
		playPause.classList.add('icon-pause');
		for (i = 0; i < len; i++) {
			playLoading[i].classList.add('active');
		}
	} else {
		player.pause();
		clearInterval(timeInterval);
		playPause.classList.remove('icon-pause');
		playPause.classList.add('icon-play');
		for (i = 0; i < len; i++) {
			playLoading[i].classList.remove('active');
		}
	}
}

// Seek Music
function seekMusic() {
	player.currentTime = seek.value;
}

// Muted Music
function mutedMusic() {
	if (player.muted) {
		player.muted = false;
		muted.classList.remove('icon-volume-mute');
		muted.classList.add('icon-volume-high');
	} else {
		player.muted = true;
		muted.classList.remove('icon-volume-high');
		muted.classList.add('icon-volume-mute');
	}
}

// Time Update
function timeUpdateMusic() {
	durationTime.innerHTML = secondToMinutes(player.duration);
	currentTime.innerHTML = secondToMinutes(player.currentTime);
	seek.max = player.duration;
	seek.value = player.currentTime;
}

// Convert Seconds to Minutes
function secondToMinutes(seconds) {
	var numMinutes = Math.floor((((seconds % 31536000) % 86400) % 3600) / 60),
			numSeconds = (((seconds % 3153600) % 86400) % 3600) % 60;

	numMinutes = numMinutes >= 10 ? numMinutes : ('0' + numMinutes);

	if (numSeconds >= 10) {
		return numMinutes + ':' + Math.round(numSeconds);
	} else {
		return numMinutes + ':0' + Math.round(numSeconds);
	}
}

// Ended Music
function endedMusic() {
	player.pause();
	player.currentTime = 0;
	playPause.classList.remove('icon-pause');
	playPause.classList.add('icon-play');
	for (i = 0; i < len; i++) {
		playLoading[i].classList.remove('active');
	}
}